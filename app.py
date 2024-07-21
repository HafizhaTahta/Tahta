from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(_name)  # Ganti _name dengan _name_

# Load the model
model = joblib.load('decision_tree_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    df = pd.DataFrame(data)
    prediction = model.predict(df)
    return jsonify(prediction.tolist())

if _name_ == '_main':  # Ganti _name dengan _name_
    app.run(debug=True)