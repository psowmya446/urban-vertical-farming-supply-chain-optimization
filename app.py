from flask import Flask, render_template, request
import os
from model_utils import predict_cost_and_footprint
from recommend import get_recommendations
from weather_api import get_weather_data, get_historical_weather, plot_weather_trends
from plot_utils import generate_resource_usage_chart
from suggestions import generate_suggestions

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    footprint = None
    recommendation = None
    city = None
    weather_data = {}
    resource_chart_exists = False
    suggestions = []
    intended_crop = None

    if request.method == "POST":
        try:
            # User inputs
            city = request.form["city"]
            intended_crop = request.form["intended_crop"]
            cost_per_unit = float(request.form["cost_per_unit"])
            transportation_time = float(request.form["transportation_time"])
            spoilage_rate = float(request.form["spoilage_rate"])
            inventory_level = float(request.form["inventory_level"])

            # Prediction
            prediction, footprint = predict_cost_and_footprint(
                cost_per_unit, transportation_time, spoilage_rate, inventory_level
            )

            # Recommendation
            features = {
                "cost_per_unit": cost_per_unit,
                "transportation_time": transportation_time,
                "spoilage_rate": spoilage_rate,
                "inventory_level": inventory_level
            }
            recommendation_list = get_recommendations(features)
            recommendation = recommendation_list[0]

            # Weather
            weather_data = get_weather_data(city)
            historical_data = get_historical_weather(city)
            plot_weather_trends(historical_data)  # Saves graph to static

            # Bar Chart: Resource Usage Comparison
            generate_resource_usage_chart(intended_crop, recommendation)
            resource_chart_exists = os.path.exists("static/resource_usage_comparison.png")

        except Exception as e:
            print("Error:", e)

    return render_template(
        "index.html",
        prediction=prediction,
        footprint=footprint,
        recommendation=recommendation,
        city=city,
        weather_data=weather_data,
        resource_chart_exists=resource_chart_exists,
        intended_crop=intended_crop,
        comparison_crop=recommendation
    )

if __name__ == "__main__":
    app.run(debug=True)
