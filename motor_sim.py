import matplotlib.pyplot as plt
import numpy as np

# --- System Modelling: Simulating a D12 Motor Thrust Curve ---
# Based on the technical specifications for a D12 motor:
# Max Thrust: ~32.90 N
# Thrust Duration: 1.60 s

# Create our time axis: 0 to 1.8 seconds (a little longer than the burn)
time = np.linspace(0, 1.8, 150)
thrust = np.zeros_like(time)

# This is a simplified mathematical model of the thrust curve graph
# It's designed to look like the chart in the motor's technical specs.
for i, t in enumerate(time):
    if t < 0.1:
        # 1. Initial Spike (0.0s to 0.1s)
        # Ramps up to a peak of ~32 N
        thrust[i] = 32.9 * (t / 0.1)
    elif t < 0.25:
        # 2. Post-Spike Drop (0.1s to 0.25s)
        # Drops from the 32.9N peak to the sustaining thrust
        thrust[i] = 32.9 - 20.9 * ((t - 0.1) / 0.15)
    elif t < 1.6:
        # 3. Sustaining Burn (0.25s to 1.6s)
        # Holds at a steady ~12N
        thrust[i] = 12.0
    else:
        # 4. Burnout (After 1.6s)
        thrust[i] = 0.0

# --- Plotting the Simulation ---
plt.figure(figsize=(10, 6))
plt.plot(time, thrust, 'b-', linewidth=2)
plt.title("Simulated Thrust Curve: D12 Motor (1.60s Burn)", fontsize=16)
plt.xlabel("Time (s)", fontsize=12)
plt.ylabel("Thrust (N)", fontsize=12)
plt.grid(True)
plt.axhline(y=12.0, color='r', linestyle='--', label='Sustaining Thrust (12N)')
plt.axhline(y=32.9, color='g', linestyle='--', label='Peak Thrust (32.9N)')
plt.legend()

# Save the plot as an image
plt.savefig('D12_Thrust_Curve_Sim.png')

print("Simulation complete. 'D12_Thrust_Curve_Sim.png' saved.")

# Display the plot
plt.show()
