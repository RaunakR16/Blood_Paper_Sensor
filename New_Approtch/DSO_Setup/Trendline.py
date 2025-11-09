import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import os
import re

# Folder path containing your CSV files
folder_path = "New_Approtch\DSO_Setup\Data\Data_06.11.2025"

# Manually specify the CSV files you want to include
manual_files = ["DryRun.CSV", "00gm.CSV", "1.25gm.CSV", "2.5gm.CSV", "05gm.CSV", "7.5gm.CSV", "10gm.CSV", "12.5gm.CSV", "15gm.CSV", "17.5gm.CSV", "20gm.CSV"]

# Create full paths for the selected files
csv_files = [os.path.join(folder_path, f) for f in manual_files]

# Sort naturally (optional)
def natural_key(text):
    return [int(s) if s.isdigit() else s for s in re.split(r'(\d+)', text)]
csv_files = sorted(csv_files, key=natural_key)

# Lists to store results
filenames = []
avg_pos_list = []
avg_neg_list = []
avg_list = []

# Process each manually selected CSV file
for file in csv_files:
    data = pd.read_csv(file, encoding='latin1')
    y = data['Volt'].values

    # Calculate thresholds
    max_amp = np.max(np.abs(y))
    prominence_threshold = 0.3 * max_amp
    distance_threshold = len(y) // 50

    # Find peaks
    pos_peaks, _ = find_peaks(y, prominence=prominence_threshold, distance=distance_threshold)
    neg_peaks, _ = find_peaks(-y, prominence=prominence_threshold, distance=distance_threshold)

    # Compute averages
    pos_values = y[pos_peaks]
    neg_values = y[neg_peaks]

    avg_pos = np.mean(pos_values)
    avg_neg = np.mean(neg_values)
    avg = (avg_pos + avg_neg) / 2

    # Store results
    filenames.append(os.path.basename(file).replace(".CSV", ""))
    avg_pos_list.append(avg_pos)
    avg_neg_list.append(avg_neg)
    avg_list.append(avg)

    print(f"Processed {os.path.basename(file)}:")
    print(f"  +ve Avg: {avg_pos:.4f} V | -ve Avg: {avg_neg:.4f} V | Avg: {avg:.4f} V\n")

# --- Plot the summarized results ---
plt.figure(figsize=(10, 6))
plt.plot(filenames, avg_pos_list, color='red', linestyle='-', linewidth=1.5, label='Average +ve Peak (V)')
plt.plot(filenames, avg_neg_list, color='green', linestyle='-', label='Average -ve Peak (V)')
plt.plot(filenames, avg_list, color='blue', linestyle='-', label='Overall Average (V)')

plt.xlabel('Data File')
plt.ylabel('Voltage (V)')
plt.title('Average Peak Voltages Across Selected Samples')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
