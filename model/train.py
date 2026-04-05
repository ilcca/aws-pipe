import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load generated data
df = pd.read_csv("data/customer_data.csv")

X = df.drop("churn", axis=1)
y = df["churn"]

# Train simple model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
joblib.dump(model, "model/model.pkl")

print("Trained model saved to model/model.pkl")