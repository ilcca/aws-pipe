import pandas as pd
import numpy as np

np.random.seed(42)

n = 1000
df = pd.DataFrame({
    "age": np.random.randint(18, 70, n),
    "tenure": np.random.randint(1, 60, n),
    "monthly_spend": np.random.uniform(10, 200, n),
    "support_calls": np.random.randint(0, 10, n),
})

# Fake churn logic
df["churn"] = ((df["support_calls"] > 5) | (df["monthly_spend"] < 30)).astype(int)

df.to_csv("data/customer_data.csv", index=False)

print("Generated fake customer data: data/customer_data.csv")