import pandas as pd
import joblib

# Load the trained model
model = joblib.load('../model/logistic_regression_model.pkl')

# Load the new data
new_data = pd.read_csv('../data/new_data.csv')

# Extract features
X_new = new_data[['Age', 'Salary']]

# Make predictions
predictions = model.predict(X_new)

# Add predictions to the new data
new_data['Purchased'] = predictions

# Save the results
new_data.to_csv('../data/predicted_data.csv', index=False)

print("Predictions saved to predicted_data.csv")
