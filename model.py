# model.py
import pickle
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Training a simple model (or you can load a pre-trained one)
X = np.array([[25, 50000], [40, 80000], [22, 20000], [30, 55000]])  # Age, Income
y = np.array([1, 0, 1, 0])  # 1 = Coffee, 0 = Tea

model = RandomForestClassifier()
model.fit(X, y)

# Save the model to a file
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
