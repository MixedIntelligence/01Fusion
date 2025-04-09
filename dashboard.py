# dashboard.py
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def visualize_predictions():
    predictions = pd.read_csv('normalized_sensor_data.csv')
    # Simulate predictions for demo
    predictions['efficiency'] = 0.85 + 0.05 * np.random.randn(len(predictions))

    plt.figure(figsize=(10, 4))
    plt.plot(predictions['time'], predictions['efficiency'], label='Predicted Efficiency')
    plt.xlabel('Time (s)')
    plt.ylabel('Efficiency Score')
    plt.title('Fusion Efficiency Prediction Over Time')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    visualize_predictions()
