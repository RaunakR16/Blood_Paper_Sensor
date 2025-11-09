import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# CSV file
data1 = pd.read_csv("New_Approtch\DSO_Setup\Data\Data_06.11.2025_REPET/20gm.CSV", encoding='latin1')

y1 = data1['Volt'].values

max_amp = np.max(np.abs(y1))

std_amp = np.std(y1)

# Auto-adjust prominence and distance based on data
prominence_threshold = 0.3 * max_amp    # ignore small ripples
distance_threshold = len(y1) // 50      # roughly 1/50th of total length between peaks

# Detect significant +ve and -ve peaks
pos_peaks, _ = find_peaks(y1, prominence=prominence_threshold, distance=distance_threshold)
neg_peaks, _ = find_peaks(-y1, prominence=prominence_threshold, distance=distance_threshold)

# Get their voltage values
pos_values = y1[pos_peaks]
neg_values = y1[neg_peaks]

# Average
avg_pos = np.mean(pos_values)
avg_neg = np.mean(neg_values)

avg = (avg_pos + avg_neg) / 2

# Print results
print(f"Total High Points Detected: {len(pos_peaks)}")
print(f"Total Low Points Detected: {len(neg_peaks)}")

print(f"Average Positive Peak Voltage: {avg_pos:.4f} V")
print(f"Average Negative Peak Voltage: {avg_neg:.4f} V")
print(f"Average Peak Voltage: {avg:.4f} V")

# Plot with marked peaks
plt.figure(figsize=(12, 6))
plt.plot(y1, label='NaCl', color='blue')
plt.plot(pos_peaks, pos_values, 'ro')
plt.plot(neg_peaks, neg_values, 'go')

# Plot average lines
plt.axhline(y=avg_pos, color='red', linestyle='--', linewidth=1.5, label=f'Avg +ve peak = {avg_pos:.4f} V')
plt.axhline(y=avg_neg, color='green', linestyle='--', linewidth=1.5, label=f'Avg -ve peak = {avg_neg:.4f} V')
plt.axhline(y=avg, color='purple', linestyle='--', linewidth=1.5, label=f'Avg = {avg:.4f} V')

plt.xlabel('Time (ms)')
plt.ylabel('Voltage (volt)')
plt.title('Time Vs Voltage with Peaks')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
