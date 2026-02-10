from flask import Flask, render_template, request, jsonify
import torch
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from models.qbert_model import QBertClassifier
from quantum.quantum_embedding import quantum_embed

app = Flask(__name__)

# Load model once
model = QBertClassifier()
model.load_state_dict(torch.load("qbert_model.pth", map_location="cpu"))
model.eval()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data["text"]

    tokens = quantum_embed(text)
    with torch.no_grad():
        output = model(tokens["input_ids"], tokens["attention_mask"])
        prediction = torch.argmax(output, dim=1).item()

    result = "Normal Communication" if prediction == 0 else "Threat Communication"

    return jsonify({
        "prediction": prediction,
        "meaning": result
    })

if __name__ == "__main__":
    app.run(debug=True)
