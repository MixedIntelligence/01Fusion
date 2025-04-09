# train_predictor.py

import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split

# Import the model
class SimpleFusionPredictor(nn.Module):
    def __init__(self):
        super(SimpleFusionPredictor, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(3, 16),
            nn.ReLU(),
            nn.Linear(16, 1)  # Predict efficiency (0–1)
        )

    def forward(self, x):
        return self.fc(x)

def load_training_data(filename='normalized_sensor_data.csv'):
    df = pd.read_csv(filename)

    # TEMPORARY — create mock 'efficiency' target column
    # Replace this with real data once available
    df['efficiency'] = 0.85 + 0.03 * df['temperature'] + \
                       0.02 * df['voltage'] - 0.01 * df['current'] + \
                       0.05 * torch.randn(len(df)).numpy()

    X = df[['temperature', 'voltage', 'current']].values.astype('float32')
    y = df['efficiency'].values.astype('float32').reshape(-1, 1)

    return train_test_split(X, y, test_size=0.2, random_state=42)

def train_model(model, train_loader, criterion, optimizer, num_epochs=100):
    for epoch in range(num_epochs):
        for batch_X, batch_y in train_loader:
            optimizer.zero_grad()
            outputs = model(batch_X)
            loss = criterion(outputs, batch_y)
            loss.backward()
            optimizer.step()

        if epoch % 10 == 0:
            print(f"Epoch {epoch} | Loss: {loss.item():.6f}")
    return model

if __name__ == "__main__":
    # Load data
    X_train, X_test, y_train, y_test = load_training_data()
    train_tensor = torch.utils.data.TensorDataset(
        torch.tensor(X_train), torch.tensor(y_train)
    )
    train_loader = torch.utils.data.DataLoader(train_tensor, batch_size=32, shuffle=True)

    # Initialize model
    model = SimpleFusionPredictor()
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    print("🚀 Starting training...")
    trained_model = train_model(model, train_loader, criterion, optimizer, num_epochs=100)

    # Save model
    torch.save(trained_model.state_dict(), 'fusion_predictor.pt')
    print("✅ Model saved as fusion_predictor.pt")
