import time
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

st.set_page_config(page_title="Industrial Monitor", layout="wide")

st.title("Industrial System Monitor Dashboard")

file_path = Path("sensor_data.csv")

if not file_path.exists():
    st.warning("No data found. Run the simulator first.")
else:
    df = pd.read_csv(file_path)

    if df.empty:
        st.warning("CSV file is empty.")
    else:
        df["timestamp"] = pd.to_datetime(df["timestamp"])

        # Show latest values
        latest = df.iloc[-1]

        st.subheader("Latest Sensor Values")

        # Check which sensors are in alert
        temp_alert = latest["temperature"] > 200
        pressure_alert = latest["pressure"] < 40
        flow_alert = latest["flow_rate"] < 90
        vibration_alert = latest["vibration"] > 0.8

        col1, col2, col3, col4 = st.columns(4)

        def metric_box(label, value, is_alert):
            color = "#ff4d4d" if is_alert else "#1f77b4"
            bg = "#ffe6e6" if is_alert else "#f0f2f6"

            st.markdown(f"""
            <div style="
                background-color: {bg};
                padding: 15px;
                border-radius: 10px;
                text-align: center;
            ">
                <h4 style="margin-bottom: 5px;">{label}</h4>
                <h2 style="color: {color}; margin: 0;">{value}</h2>
            </div>
            """, unsafe_allow_html=True)

        with col1:
            metric_box("Temperature (°F)", latest["temperature"], temp_alert)

        with col2:
            metric_box("Pressure (psi)", latest["pressure"], pressure_alert)

        with col3:
            metric_box("Flow Rate (gpm)", latest["flow_rate"], flow_alert)

        with col4:
            metric_box("Vibration (in/s)", latest["vibration"], vibration_alert)
       # 🚨 Alert Status (Detailed)
        alerts = []

        if latest["temperature"] > 200:
            alerts.append("🔥 Temperature too high")

        if latest["pressure"] < 40:
            alerts.append("⚠️ Pressure too low")

        if latest["flow_rate"] < 90:
            alerts.append("💧 Flow rate too low")

        if latest["vibration"] > 0.8:
            alerts.append("⚡ Vibration too high")

        if alerts:
            st.error("🚨 ALERT: System issues detected!")
            for alert in alerts:
                st.markdown(f"- {alert}")
        else:
            st.success("✅ System operating normally")

        st.subheader("Sensor Trends")

        sensors = ["temperature", "pressure", "flow_rate", "vibration"]
        selected_sensor = st.selectbox("Select Sensor", sensors)

        fig, ax = plt.subplots()
        ax.plot(df["timestamp"], df[selected_sensor], marker="o")
        # Add threshold lines
        # Add threshold lines
        if selected_sensor == "temperature":
            ax.axhline(200, linestyle="--", label="Max Safe Limit")
        elif selected_sensor == "pressure":
            ax.axhline(40, linestyle="--", label="Min Safe Limit")
        elif selected_sensor == "flow_rate":
            ax.axhline(90, linestyle="--", label="Min Safe Limit")
        elif selected_sensor == "vibration":
            ax.axhline(0.8, linestyle="--", label="Max Safe Limit")
            ax.legend()
        ax.set_title(f"{selected_sensor.capitalize()} Over Time")
        ax.set_xlabel("Time")
        ax.set_ylabel(selected_sensor)

        plt.xticks(rotation=45)
        plt.tight_layout()

        st.pyplot(fig)

        # Auto refresh every 2 seconds
        time.sleep(2)
        st.rerun()

        