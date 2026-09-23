import pandas as pd

# 1. Create the DataFrame
surveillance_df = pd.DataFrame({
    "patient_id": [1, 2, 3, 4, 5],
    "age": [28, None, 45, 52, 19],
    "fever_temp": [38.5, 39.1, None, 37.8, 36.6],
    "risk_level": ["High", "High", "Medium", "Low", "Low"]
})

# Display the original DataFrame
print("Original DataFrame:")
print(surveillance_df)


# 2. Inspect missing values
print("\nMissing values in each column:")
print(surveillance_df.isnull().sum())


# Impute missing age value with the column mean
age_mean = surveillance_df["age"].mean()
surveillance_df["age"] = surveillance_df["age"].fillna(age_mean)


# Impute missing fever_temp value with the column median
fever_median = surveillance_df["fever_temp"].median()
surveillance_df["fever_temp"] = surveillance_df["fever_temp"].fillna(fever_median)


# Display the DataFrame after imputation
print("\nDataFrame after imputing missing values:")
print(surveillance_df)


# 3. Filter patients older than 25 AND fever temperature greater than 37.5
filtered_patients = surveillance_df[
    (surveillance_df["age"] > 25) &
    (surveillance_df["fever_temp"] > 37.5)
]

print("\nPatients older than 25 with fever_temp greater than 37.5:")
print(filtered_patients)


# 4. One-Hot Encoding of risk_level
surveillance_df = pd.get_dummies(
    surveillance_df,
    columns=["risk_level"],
    dtype=int
)

print("\nDataFrame after One-Hot Encoding:")
print(surveillance_df)
