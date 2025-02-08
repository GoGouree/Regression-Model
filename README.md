# Logistic Regression Model

This project demonstrates the use of a logistic regression model to predict whether an individual will purchase a product based on their age and salary.

## Project Structure

```
Regression-Model/
├── data/
│   ├── logistic_regression_sample.csv  # The dataset used for training and testing
│   ├── new_data.csv                    # New data for making predictions
│   ├── predicted_data.csv              # Predictions on the new data (generated)
│   ├── predicted_test_data.csv         # Predictions on the test data (generated)
├── scripts/
│   ├── logistic_regression.py          # Script to train and save the model
│   ├── predict_new_data.py             # Script to load the model and make predictions
│   ├── evaluate_model.py               # Script to evaluate the model accuracy
├── model/
│   └── logistic_regression_model.pkl   # The saved trained model
├── venv/
├── .gitignore
├── README.md
└── requirements.txt
```

## Setup

1. **Clone the Repository**
    ```bash
    git clone <repository-url>
    cd Regression-Model
    ```

2. **Create and Activate Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Train the Model
```bash
cd scripts
python logistic_regression.py
```

### Make Predictions on New Data
```bash
python predict_new_data.py
```

### Evaluate the Model Accuracy
```bash
python evaluate_model.py
```

## Data Files

- `data/logistic_regression_sample.csv`: The dataset used for training and testing.
- `data/new_data.csv`: The new data for which predictions are to be made.
- `data/predicted_data.csv`: The file where predictions on new data will be saved.
- `data/predicted_test_data.csv`: The file where predictions on test data will be saved.