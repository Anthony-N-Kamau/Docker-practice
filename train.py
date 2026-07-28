from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
import os

print("Loading data...")
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training model...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

accuracy = accuracy_score(y_test, model.predict(X_test))
print(f"Test accuracy: {accuracy:.4f}")

os.makedirs("/app/output", exist_ok=True)
with open("/app/output/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved to /app/output/model.pkl")
