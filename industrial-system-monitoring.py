import random
import time
import csv
import logging
from datetime import datetime

# Safe operating ranges
LIMITS = {
    "temperature": (180, 220),   # Fahrenheit
    "pressure": (40, 60),        # PSI
    "flow_rate": (90, 110),      # GPM
    "vibration": (0.2, 0.8)      # in/s
}

# Configure alert logging
logging.basicConfig(
    filename="alerts.log",
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def generate_sensor_data():
    """Generate normal sensor readings with occasional anomalies."""
    data = {
        "temperature": round(random.uniform(185, 215), 2),
        "pressure": round(random.uniform(45, 55), 2),
        "flow_rate": round(random.uniform(95, 105), 2),
        "vibration": round(random.uniform(0.3, 0.7), 2)
    }

    # 15% chance to inject an abnormal reading
    if random.random() < 0.15:
        sensor = random.choice(list(data.keys()))

        if sensor == "temperature":
            data[sensor] = round(random.uniform(230, 260), 2)
        elif sensor == "pressure":
            data[sensor] = round(random.uniform(10, 35), 2)
        elif sensor == "flow_rate":
            data[sensor] = round(random.uniform(60, 85), 2)
        elif sensor == "vibration":
            data[sensor] = round(random.uniform(0.9, 1.5), 2)

    return data

def check_anomalies(data):
    """Check readings against safe limits."""
    alerts = []

    for sensor, value in data.items():
        low, high = LIMITS[sensor]

        if value < low:
            alerts.append(f"{sensor.upper()} LOW: {value}")
        elif value > high:
            alerts.append(f"{sensor.upper()} HIGH: {value}")

    return alerts

def save_to_csv(data):
    """Save sensor readings to CSV."""
    file_name = "sensor_data.csv"

    file_exists = False
    try:
        with open(file_name, "r"):
            file_exists = True
    except FileNotFoundError:
        pass

    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["timestamp", "temperature", "pressure", "flow_rate", "vibration"])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            data["temperature"],
            data["pressure"],
            data["flow_rate"],
            data["vibration"]
        ])

def main():
    print("Industrial System Monitor Simulator")
    print("-" * 45)

    while True:
        data = generate_sensor_data()
        alerts = check_anomalies(data)

        print(
            f"Temp: {data['temperature']}°F | "
            f"Pressure: {data['pressure']} psi | "
            f"Flow: {data['flow_rate']} gpm | "
            f"Vibration: {data['vibration']} in/s"
        )

        if alerts:
            print("STATUS: ALERT")
            for alert in alerts:
                print(" -", alert)
                logging.warning(alert)
        else:
            print("STATUS: NORMAL")

        save_to_csv(data)
        print()

        time.sleep(1)

if __name__ == "__main__":
    main()