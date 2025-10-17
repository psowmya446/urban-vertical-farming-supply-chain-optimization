import pickle
import numpy as np

# Load trained model
model_path = "models/cost_prediction_model.pkl"
model = pickle.load(open(model_path, "rb"))

def predict_cost_and_footprint(cost_per_unit, transportation_time, spoilage_rate, inventory_level):
    # Input features
    features = np.array([[cost_per_unit, transportation_time, spoilage_rate, inventory_level]])
    
    # Prediction
    predicted_cost = model.predict(features)[0]
    
    # Sample carbon footprint logic
    footprint = (transportation_time * 0.5) + (spoilage_rate * 0.3) + (inventory_level * 0.01)

    return predicted_cost, footprint
