# model_predictor.py
import pandas as pd
import torch
import torch.nn as nn

class SimpleFusionPredictor(nn.Module):
    def __init__(self):
        super(SimpleFusionPredictor, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(3, 16),
            nn.ReLU(),
            nn.Linear(16, 1)  # Predicts: Efficiency score (0–1)
        )

    def forward(self, x):
        return self.fc(x)

def load_data():
    df = pd.read_csv('normalized_sensor_data.csv')
    features = df[['temperature', 'voltage', 'current']].values.astype('float32')
    return torch.tensor(features)

def run_model():
    model = SimpleFusionPredictor()
    model.eval()
    x = load_data()
    with torch.no_grad():
        predictions = model(x)
    return predictions.numpy()

if __name__ == "__main__":
    results = run_model()
    print(f"✅ Predicted efficiency (first 5 rows):\n{results[:5]}")
