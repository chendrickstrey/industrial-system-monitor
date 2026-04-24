# Industrial System Monitor Simulator

A Python-based industrial monitoring system that simulates real-time sensor data, detects anomalies, and visualizes system performance through an interactive dashboard.

This project models key industrial parameters including temperature, pressure, flow rate, and vibration—similar to real-world monitoring systems used in manufacturing and energy environments.

---

## 🚀 Features

- Real-time sensor data simulation
- Automated anomaly detection (threshold-based)
- Alert logging to file (`alerts.log`)
- Continuous data storage (`sensor_data.csv`)
- Interactive dashboard using Streamlit
- Sensor trend visualization with threshold indicators
- Highlighted alerts for failing sensors

---

## 🛠 Technologies Used

- Python
- Streamlit
- Pandas
- Matplotlib
- Logging
- CSV File Handling

---

## ⚙️ How It Works

The system continuously:

1. Generates simulated sensor readings  
2. Compares values against safe operating thresholds  
3. Logs anomalies to a file  
4. Stores all data in a CSV file  
5. Displays real-time updates in a dashboard  

---

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install streamlit pandas matplotlib