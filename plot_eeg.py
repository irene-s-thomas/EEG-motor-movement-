import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the PhysioNet subset
df = pd.read_csv('physionet_sample.csv')

# 2. Create a figure with multiple "subplots" (one for each electrode)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# 3. Plot Electrode Cz (Center of the head)
ax1.plot(df['time'], df['Cz'], color='blue', linewidth=1.5)
ax1.set_title('Electrode Cz (Mid-Line)')
ax1.set_ylabel('Voltage (μV)')
ax1.grid(True, alpha=0.3)

# 4. Plot Electrode C4 (Right side of the head)
ax2.plot(df['time'], df['C4'], color='red', linewidth=1.5)
ax2.set_title('Electrode C4 (Right Motor Cortex)')
ax2.set_ylabel('Voltage (μV)')
ax2.set_xlabel('Time (seconds)')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
