from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open("model/knn_model.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            age = int(request.form["age"])
            bmi = float(request.form["bmi"])
            bp = int(request.form["blood_pressure"])
            glucose = float(request.form["glucose"])
            activity = int(request.form["activity"])
            history = int(request.form["family_history"])

            features = np.array([[age, bmi, bp, glucose, activity, history]])
            prediction = model.predict(features)[0]

            risk_map = {0: "Low Risk", 1: "Moderate Risk", 2: "High Risk"}
            result = risk_map.get(prediction, "Unknown")

            return render_template("index.html", prediction_text=f"Predicted Health Risk: {result}")
        except Exception as e:
            return render_template("index.html", prediction_text=f"Error: {str(e)}")

    return render_template("index.html", prediction_text=None)

if __name__ == "__main__":
    app.run(debug=True)
