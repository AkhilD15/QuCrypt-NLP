import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import torch
from models.qbert_model import QBertClassifier
from quantum.quantum_embedding import quantum_embed

# Load trained model
model = QBertClassifier()
model.load_state_dict(torch.load("qbert_model.pth", map_location="cpu"))
model.eval()

# ---- SINGLE INPUT TEXT ----
text = "The █████ discussed █████ at ████"

# Tokenize & embed
tokens = quantum_embed(text)

# Inference
with torch.no_grad():
    output = model(tokens["input_ids"], tokens["attention_mask"])
    prediction = torch.argmax(output, dim=1).item()

# Output explanation
label_name = "Normal" if prediction == 0 else "Threat"

print("Input Text:", text)
print("Predicted Class:", prediction)
print("Meaning:", label_name)
