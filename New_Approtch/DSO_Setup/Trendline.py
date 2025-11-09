import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import glob
import os

# Folder path containing your CSV files
folder_path = "New_Approtch\DSO_Setup\Data\Data_06.11.2025"


# Get all CSV files in the folder
csv_files = glob.glob(os.path.join(folder_path, "*.CSV"))

# Lists to store results
filenames = []
avg_pos_list = []
avg_neg_list = []
avg_list = []
    
# Process each CSV file
for file in csv_files:
    data = pd.read_csv(file, encoding='latin1')
    y = data['Volt'].values

    # Calculate thresholds
    max_amp = np.max(np.abs(y))
    std_amp = np.std(y)
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
plt.plot(filenames, avg_neg_list, 'g-o', label='Average -ve Peak (V)')
plt.plot(filenames, avg_list, 'b--o', label='Overall Average (V)')

plt.xlabel('Data File')
plt.ylabel('Voltage (V)')
plt.title('Average Peak Voltages Across Multiple Samples')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
