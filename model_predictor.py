# model_predictor.py

import pandas as pd
import torch
import torch.nn as nn
import os

MODEL_PATH = 'fusion_predictor.pt'
DATA_PATH = 'normalized_sensor_data.csv'

class SimpleFusionPredictor(nn.Module):
    def __init__(self):
        super(SimpleFusionPredictor, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(3, 16),
            nn.ReLU(),
            nn.Linear(16, 1)
        )

    def forward(self, x):
        return self.fc(x)

def load_data():
    df = pd.read_csv(DATA_PATH)
    features = df[['temperature', 'voltage', 'current']].values.astype('float32')
    return torch.tensor(features), df['time'].values

def run_model():
    x, time_vals = load_data()
    model = SimpleFusionPredictor()

    if os.path.exists(MODEL_PATH):
        model.load_state_dict(torch.load(MODEL_PATH))
        model.eval()
        with torch.no_grad():
            predictions = model(x)
        return time_vals, predictions.numpy()
    else:
        print("⚠️ Trained model not found. Run `train_predictor.py` first.")
        return time_vals, None

if __name__ == "__main__":
    time_vals, results = run_model()

    if results is not None:
        print("✅ Model predictions (first 5):")
        for i in range(5):
            print(f"t={time_vals[i]:.2f}s → Efficiency: {results[i][0]:.4f}")
