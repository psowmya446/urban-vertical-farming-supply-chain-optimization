import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import StackingRegressor, RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import joblib
import os

# Load dataset
df = pd.read_csv('data/supply_chain_optimization_past_seasonal_dataset.csv')
df.dropna(inplace=True)

# Feature Engineering
df['spoilage_per_day'] = df['spoilage_rate'] / df['transportation_time']
df['cost_efficiency'] = df['cost_per_unit'] / (df['inventory_level'] + 1)

# Features and target
X = df[['transportation_time', 'spoilage_rate', 'inventory_level',
        'spoilage_per_day', 'cost_efficiency']]
y = df['cost_per_unit']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Save scaler
joblib.dump(scaler, 'models/scaler.pkl')

# Define base models and meta-model
base_models = [
    ('lr', LinearRegression()),
    ('dt', DecisionTreeRegressor(random_state=42)),
    ('knn', KNeighborsRegressor())
]
meta_model = RandomForestRegressor(n_estimators=100, random_state=42)

# Stacking Regressor
model = StackingRegressor(estimators=base_models, final_estimator=meta_model)
model.fit(X_train_scaled, y_train)

# Predict and Evaluate
y_pred = model.predict(X_test_scaled)
r2 = r2_score(y_test, y_pred)

# Save model
joblib.dump(model, 'models/supply_chain_model.pkl')

# Create static directory if it doesn't exist
os.makedirs('static', exist_ok=True)

# Plot actual vs predicted
plt.figure(figsize=(8, 5))
plt.plot(y_test.values, label='Actual', marker='o')
plt.plot(y_pred, label='Predicted', marker='x')
plt.title('📈 Actual vs Predicted Cost per Unit')
plt.xlabel('Sample Index')
plt.ylabel('Cost per Unit')
plt.legend()
plt.tight_layout()
plt.savefig('static/actual_vs_predicted.png')
plt.close()

print("✅ Model trained successfully!")
print(f"🔍 R² Score (Accuracy): {r2:.4f}")
