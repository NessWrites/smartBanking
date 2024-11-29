import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

# Example Dataset
data = pd.DataFrame({
    'x1': [1, 2, 3, 4],
    'x2': [5, 6, 7, 8],
    'y': [0, 1, 0, 1]
})

# Features and Target
X = data[['x1', 'x2']]
y = data['y']

# Fit Logistic Regression Model
model = LogisticRegression()
model.fit(X, y)

# Calculate Log Odds (Manual)
intercept = model.intercept_[0]
coefficients = model.coef_[0]
log_odds = intercept + np.dot(X, coefficients)

# Calculate Odds and Probability (Manual)
odds = np.exp(log_odds)
probabilities = odds / (1 + odds)

# Use predict_proba() to Calculate Probabilities
predicted_probs = model.predict_proba(X)[:, 1]

# Results
print(pd.DataFrame({'LogOdds': log_odds, 'Odds': odds, 'Probabilities': probabilities}))
print(predicted_probs)
