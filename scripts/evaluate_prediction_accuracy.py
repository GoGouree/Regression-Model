import pandas as pd
import joblib
from sklearn.metrics import accuracy_score

# Load the trained model
model = joblib.load('../model/logistic_regression_model.pkl')

# Load the test data with actual values for evaluation
test_data = pd.read_csv('../data/logistic_regression_sample.csv')

# Extract features and actual target
X_test = test_data[['Age', 'Salary']]
y_actual = test_data['Purchased']

# Make predictions
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_actual, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Add predictions to the test data
test_data['Predicted_Purchased'] = y_pred

# Save the results
test_data.to_csv('../data/predicted_test_data.csv', index=False)
