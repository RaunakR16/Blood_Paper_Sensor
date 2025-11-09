import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import os

# --------------------------------------------
# Define your CSV files in order
# --------------------------------------------
data_files = [
    r"New_Approtch\DSO_Setup\Data\Data_06.11.2025/DryRun.CSV",
    r"New_Approtch\DSO_Setup\Data\Data_06.11.2025/00gm.CSV",
    r"New_Approtch\DSO_Setup\Data\Data_06.11.2025/1.25gm.CSV",
    r"New_Approtch\DSO_Setup\Data\Data_06.11.2025/2.5gm.CSV",
    r"New_Approtch\DSO_Setup\Data\Data_06.11.2025/05gm.CSV"
]

# --------------------------------------------
# Storage for results
# --------------------------------------------
file_labels = []
avg_pos_list = []
avg_neg_list = []
avg_combined_list = []

# --------------------------------------------
# Function to process one file
# --------------------------------------------
def analyze_file(file_path):
    data = pd.read_csv(file_path, encoding='latin1')
    y = data['Volt'].values

    max_amp = np.max(np.abs(y))
    prominence_threshold = 0.3 * max_amp
    distance_threshold = len(y) // 50

    pos_peaks, _ = find_peaks(y, prominence=prominence_threshold, distance=distance_threshold)
    neg_peaks, _ = find_peaks(-y, prominence=prominence_threshold, distance=distance_threshold)

    pos_values = y[pos_peaks]
    neg_values = y[neg_peaks]

    avg_pos = np.mean(pos_values) if len(pos_values) > 0 else 0
    avg_neg = np.mean(neg_values) if len(neg_values) > 0 else 0
    avg_all = (avg_pos + avg_neg) / 2

    return avg_pos, avg_neg, avg_all

# --------------------------------------------
# Loop through all files
# --------------------------------------------
for i, f in enumerate(data_files, start=1):
    if not os.path.exists(f):
        print(f" File not found: {f}")
        continue

    avg_pos, avg_neg, avg_all = analyze_file(f)
    file_labels.append(f"Data{i:02d}")
    avg_pos_list.append(avg_pos)
    avg_neg_list.append(avg_neg)
    avg_combined_list.append(avg_all)

    print(f" {os.path.basename(f)} processed:")
    print(f"   Avg +ve Peak: {avg_pos:.4f} V | Avg -ve Peak: {avg_neg:.4f} V | Combined Avg: {avg_all:.4f} V\n")

# --------------------------------------------
# Plot the results
# --------------------------------------------
plt.figure(figsize=(10, 6))
plt.plot(file_labels, avg_pos_list, 'ro-', label='Avg +ve Peak Voltage')
plt.plot(file_labels, avg_neg_list, 'go-', label='Avg -ve Peak Voltage')
plt.plot(file_labels, avg_combined_list, 'bo-', label='Combined Avg Voltage')

plt.title('Average Peak Voltages Across Multiple Data Files')
plt.xlabel('Data File Number')
plt.ylabel('Voltage (V)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
