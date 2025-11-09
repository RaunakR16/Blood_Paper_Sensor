import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import os

# CSV files in order
data_files = [
    r"New_Approtch\DSO_Setup\Data\Data_06.11.2025/DryRun.CSV",
    r"New_Approtch\DSO_Setup\Data\Data_06.11.2025/00gm.CSV",
    r"New_Approtch\DSO_Setup\Data\Data_06.11.2025/1.25gm.CSV",
    r"New_Approtch\DSO_Setup\Data\Data_06.11.2025/2.5gm.CSV",
    r"New_Approtch\DSO_Setup\Data\Data_06.11.2025/05gm.CSV",
    r"New_Approtch\DSO_Setup\Data\Data_06.11.2025/07.5gm.CSV",
    r"New_Approtch\DSO_Setup\Data\Data_06.11.2025/10gm.CSV",    
    r"New_Approtch\DSO_Setup\Data\Data_06.11.2025/12.5gm.CSV",
    r"New_Approtch\DSO_Setup\Data\Data_06.11.2025/15gm.CSV",
    r"New_Approtch\DSO_Setup\Data\Data_06.11.2025/17.5gm.CSV",
    r"New_Approtch\DSO_Setup\Data\Data_06.11.2025/20gm.CSV"
]

file_labels = []
avg_pos_list = []
avg_neg_list = []
avg_combined_list = []

# File Processing
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

# Loop through files
for f in data_files:
    if not os.path.exists(f):
        print(f"File not found: {f}")
        continue

    avg_pos, avg_neg, avg_all = analyze_file(f)
    label = os.path.splitext(os.path.basename(f))[0]  # Extract filename 
    file_labels.append(label)
    avg_pos_list.append(avg_pos)
    avg_neg_list.append(avg_neg)
    avg_combined_list.append(avg_all)

    print(f"{label} processed:")
    print(f"   Avg +ve Peak: {avg_pos:.4f} V | Avg -ve Peak: {avg_neg:.4f} V | Combined Avg: {avg_all:.4f} V\n")

# Convert labels to numeric x-axis positions
x = np.arange(len(file_labels))

# Fit a linear trend line to Avg +ve peaks
z = np.polyfit(x, avg_pos_list, 1)     # 1st-degree polynomial (linear)
p = np.poly1d(z)

# Generate trendline values
trend_pos = p(x)

# Fit a linear trend line to Avg +ve peaks
a = np.polyfit(x, avg_neg_list, 1)     # 1st-degree polynomial (linear)
b = np.poly1d(a)

# Generate trendline values
trend_neg = b(x)


# Plot results
plt.figure(figsize=(10, 6))
plt.plot(file_labels, avg_pos_list, color='red', label='Avg +ve Peak Voltage')
plt.plot(file_labels, avg_neg_list, color='green', label='Avg -ve Peak Voltage')
plt.plot(file_labels, avg_combined_list, color='blue', label='Avg Voltage')

# Add trend line for +ve peaks
plt.plot(file_labels, trend_pos, color='orange', linestyle='--', linewidth=2, label=f'Trend Line +ve Peaks eq:{z[0]:.4f}x + {z[1]:.4f}')
plt.plot(file_labels, trend_neg, color='black', linestyle='--', linewidth=2, label=f'Trend Line +ve Peaks eq:{a[0]:.4f}x + {a[1]:.4f}')

plt.title('NaCl Analysis')
plt.xlabel('NaCl quantity (gm) in 50ml water')
plt.ylabel('Voltage (V)')
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Display equation of trend line
print(f"Trend Line Equation for +ve Peaks: y = {z[0]:.4f}x + {z[1]:.4f}")
