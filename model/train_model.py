import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pickle

df = pd.read_csv("dataset/knn_health_risk_dataset.csv")

X = df[["Age", "BMI", "BloodPressure", "Glucose", "ActivityLevel", "FamilyHistory"]]
y = df["RiskLevel"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

pickle.dump(model, open("model/knn_model.pkl", "wb"))
print("Model trained and saved successfully.")
