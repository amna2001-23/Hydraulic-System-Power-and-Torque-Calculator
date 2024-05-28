import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Function to calculate power and torque
def calculate_power_torque(load, speed, max_pressure, rpm):
    # Assuming efficiency of 100%
    # Calculate power (Power = Force * Velocity)
    power = load * speed  # in Watts
    # Calculate torque (Torque = Power / (2 * pi * RPM / 60))
    torque = power / (2 * np.pi * rpm / 60)  # in Nm
    return power, torque

# Streamlit app layout

st.title("Hydraulic System Power and Torque Calculator")
st.image("unnamed.jpg", caption="Hydraulic Circuit Diagram", use_column_width=True,)



st.sidebar.header("Input Parameters")

# User inputs
load = st.sidebar.slider("Load (N)", 0, 2000, 1000)
speed = st.sidebar.slider("Speed (m/s)", 0.05, 0.1, 0.075)
max_pressure = st.sidebar.slider("Max Pressure (bar)", 0, 150, 150)
rpm = st.sidebar.slider("RPM", 0, 1500, 1500)

# Calculate power and torque
power, torque = calculate_power_torque(load, speed, max_pressure, rpm)

# Display results
st.write(f"### Calculated Power: {power:.2f} W")
st.write(f"### Calculated Torque: {torque:.2f} Nm")

# Plotting
fig, ax = plt.subplots()
ax.bar(['Power (W)', 'Torque (Nm)'], [power, torque], color=['blue', 'green'])
ax.set_ylabel('Magnitude')
ax.set_title('Power and Torque')
st.pyplot(fig)
