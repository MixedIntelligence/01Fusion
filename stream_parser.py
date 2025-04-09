# Simulates thermal + voltage sensor readings, adds noise, normalizes python

# stream_parser.py
import numpy as np
import pandas as pd

def generate_sensor_data(num_points=1000):
    """Simulates sensor input data with noise"""
    time = np.linspace(0, 100, num_points)
    temperature = 300 + 5 * np.sin(0.1 * time) + np.random.normal(0, 0.5, num_points)
    voltage = 1.5 + 0.3 * np.cos(0.2 * time) + np.random.normal(0, 0.05, num_points)
    current = 0.8 + 0.1 * np.sin(0.05 * time + 1) + np.random.normal(0, 0.02, num_points)

    data = pd.DataFrame({
        'time': time,
        'temperature': temperature,
        'voltage': voltage,
        'current': current
    })

    return data

def normalize(df):
    return (df - df.mean()) / df.std()

if __name__ == "__main__":
    df = generate_sensor_data()
    df_norm = normalize(df[['temperature', 'voltage', 'current']])
    df_norm['time'] = df['time']
    df_norm.to_csv('normalized_sensor_data.csv', index=False)
    print("✅ Sensor data generated and normalized.")
