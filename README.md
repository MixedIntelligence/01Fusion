# 01Fusion

# Plasma MXI – Fusion Core Monitor

Welcome to the **Fusion Stack** of Plasma MXI: an open platform to explore AI-optimized fusion and LENR energy systems. This repo is the foundation for real-time monitoring, sensor data ingestion, and ML-based optimization of experimental fusion environments.

## 📦 Repos

- `fusion-core-monitor` – sensor inputs + data stream handling
- `plasma-ml-optimizer` – machine learning models for optimization + prediction
- `lenr-sim-lab` – tools for LENR material modeling + heat flow sim
- `reactor-control-suite` – interface layer for test rig automation

## 🔧 Fusion-Core-Monitor Structure

fusion-core-monitor/ 
├── src/ │ 
├── sensors/ # Sensor drivers, e.g., temp, B-field, voltage │ 
├── stream/ # Real-time ingestion + format conversion │ 
├── calibration/ # Sensor calibration + safety checks 
├── data/ # Sample test sets, training data 
├── scripts/ # CLI tools for bootstrapping rigs 
├── notebooks/ #
