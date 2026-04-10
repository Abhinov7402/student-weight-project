import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# 1. Generate Synthetic Data
np.random.seed(42)
heights = np.random.normal(68, 4, 150)  # Mean 68", Std Dev 4"
# Weight roughly follows: height * 2.5 - 20 + some noise
weights = (heights * 2.5) - 20 + np.random.normal(0, 5, 150)

# Reshape for scikit-learn
X = heights.reshape(-1, 1)
y = weights

# 2. Build and Train the Model
model = LinearRegression()
model.fit(X, y)

# 3. Interactive Terminal Input
print("--- Student Weight Predictor ---")
try:
    user_height = float(input("Enter student height in inches: "))
    prediction = model.predict([[user_height]])
    print(f"Predicted weight: {prediction[0]:.2f} lbs")
except ValueError:
    print("Please enter a valid numerical value for height.")