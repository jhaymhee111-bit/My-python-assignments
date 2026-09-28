# Import the required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------------------------
# 1. CREATE A SYNTHETIC DATAFRAME
# --------------------------------------------

# Set a random seed so the results can be reproduced
np.random.seed(42)

# Create 100 records
n = 100

# Create the DataFrame
df = pd.DataFrame({
    "age": np.random.randint(18, 80, n),

    # Generate temperatures around 37°C
    "fever_temperature": np.random.normal(38, 1.2, n),

    # Generate recovery days between approximately 2 and 20
    "recovery_days": np.random.randint(2, 21, n),

    # Randomly assign each person to a risk group
    "risk_factor": np.random.choice(
        ["Low Risk", "High Risk"],
        size=n
    )
})

# Display the first 5 records
print("First 5 records:")
print(df.head())

print("\nDataset information:")
print(df.info())

# --------------------------------------------
# 2. HISTOGRAM + KDE FOR FEVER TEMPERATURE
# --------------------------------------------

plt.figure(figsize=(8, 5))

sns.histplot(
    data=df,
    x="fever_temperature",
    kde=True,
    bins=15
)

plt.title("Distribution of Fever Temperature")
plt.xlabel("Fever Temperature (°C)")
plt.ylabel("Frequency")

# Save the figure
plt.savefig("eda_fever_temperature.png", dpi=300, bbox_inches="tight")

# Display the figure
plt.show()

# --------------------------------------------
# 3. BOX PLOT OF RECOVERY DAYS BY RISK
# --------------------------------------------

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="risk_factor",
    y="recovery_days"
)

plt.title("Recovery Days by Risk Factor")
plt.xlabel("Risk Factor")
plt.ylabel("Recovery Days")

# Save the figure
plt.savefig("eda_recovery_boxplot.png", dpi=300, bbox_inches="tight")

# Display the figure
plt.show()

# --------------------------------------------
# 4. CORRELATION HEATMAP
# --------------------------------------------

# Select only numerical columns
numerical_data = df[
    ["age", "fever_temperature", "recovery_days"]
]

# Calculate the correlation matrix
correlation_matrix = numerical_data.corr()

# Create the heatmap
plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation_matrix,
    annot=True,       # Display correlation values
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5
)

plt.title("Correlation Heatmap")

# Save the heatmap
plt.savefig("eda_heatmap.png", dpi=300, bbox_inches="tight")

# Display the heatmap
plt.show()

# --------------------------------------------
# END OF SCRIPT
# --------------------------------------------

print("\nEDA analysis completed successfully!")
print("The following PNG files have been saved:")
print("1. eda_fever_temperature.png")
print("2. eda_recovery_boxplot.png")
print("3. eda_heatmap.png")
