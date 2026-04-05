import joblib

# Load model
model = joblib.load("model/model.pkl")

def predict(data):
    return model.predict([data]).tolist()

# Example
sample = [35, 12, 200, 4]  # age, tenure, monthly_spend, support_calls
print("Prediction for sample:", predict(sample))