import pickle
import numpy as np

# Load the trained recommendation model
model_path = "models/recommendation_model.pkl"
recommendation_model = pickle.load(open(model_path, "rb"))

def get_recommendations(features):
    input_features = np.array([[ 
        features["cost_per_unit"],
        features["transportation_time"],
        features["spoilage_rate"],
        features["inventory_level"]
    ]])
    prediction = recommendation_model.predict(input_features)
    return [prediction[0]]  # Return as a list for consistency

# Crop resource chart for comparison display
resource_chart = {
    "Tomatoes": {"Water": 600, "Fertilizer": 50},
    "Cucumbers": {"Water": 500, "Fertilizer": 45},
    "Peppers": {"Water": 550, "Fertilizer": 40},
    "Lettuce": {"Water": 400, "Fertilizer": 30},
    "Spinach": {"Water": 450, "Fertilizer": 35},
    "Carrots": {"Water": 520, "Fertilizer": 42},
    "Beans": {"Water": 480, "Fertilizer": 38},
    "Onions": {"Water": 530, "Fertilizer": 46},
    "Cabbage": {"Water": 560, "Fertilizer": 43}
}
