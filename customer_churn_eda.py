import numpy as np
import pandas as pd

np.random.seed(42)
n = 100

df = pd.DataFrame({
    "ID": range(1, n + 1),
    "Gender": np.random.choice(["Male", "Female"], n),
    "Tenure": np.random.randint(1, 73, n),
    "Contract": np.random.choice(
        ["Month-to-month", "One year", "Two year"], n),
    "Charges": np.random.uniform(20, 120, n).round(2),
    "Churn": np.random.choice(["Yes", "No"], n, p=[0.3, 0.7])
})

print("First 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

df = df.drop_duplicates()
df["Tenure"] = df["Tenure"].fillna(df["Tenure"].median())

print("\nChurn Rate:")
print(df["Churn"].value_counts(normalize=True) * 100)

print("\nChurn by Contract:")
print(pd.crosstab(df["Contract"], df["Churn"]))

print("\nAverage Charges:")
print(df.groupby("Churn")["Charges"].mean())
