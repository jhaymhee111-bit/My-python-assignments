import numpy as np

# 1. Create the patient data array
# Columns: Height (meters), Weight (kg)
patient_data = np.array([
    [1.75, 70],
    [1.60, 50],
    [1.80, 90],
    [1.65, 65]
])

# 2. Extract heights and weights using vectorized NumPy operations
heights = patient_data[:, 0]
weights = patient_data[:, 1]

# Calculate BMI for all patients
bmi = weights / (heights ** 2)

# 3. Calculate mean, maximum, and standard deviation
mean_bmi = np.mean(bmi)
max_bmi = np.max(bmi)
std_bmi = np.std(bmi)

# Print the results
print("Patient Data:")
print(patient_data)

print("\nHeights:")
print(heights)

print("\nWeights:")
print(weights)

print("\nBMI:")
print(bmi)

print("\nMean BMI:", mean_bmi)
print("Maximum BMI:", max_bmi)
print("Standard Deviation of BMI:", std_bmi)

