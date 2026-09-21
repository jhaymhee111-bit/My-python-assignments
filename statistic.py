import numpy as np
actual = np . array([100, 150, 200])
predicted = np . array([110, 140, 210])
# Vectorized Error Calculation
errors = predicted - actual
squared_errors = errors ** 2
mse = np.mean(squared_errors)
print(f"Errors: {errors}")
print(f"Mean Squared Error (MSE): {mse: .2f}")
