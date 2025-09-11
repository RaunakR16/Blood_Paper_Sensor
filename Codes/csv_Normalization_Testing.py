import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Data
data6 = pd.read_csv("Data/P2_26.08.2025/06.09.2025/NEW_Sample/118_paper_impedance_data.csv", encoding='latin1')
data7 = pd.read_csv("C:/Users/rauna/Downloads/Blood_Paper_Sensor/Data/P2_26.08.2025/02.09.2025/NEW_Sample/118_paper_impedance_data.csv", encoding='latin1')
data3 = pd.read_csv("Data/P2_26.08.2025/02.09.2025\OLD_Sample/118_paper_impedance_data.csv", encoding='latin1')

data8 = pd.read_csv("Data\P2_26.08.2025/06.09.2025/OLD_Sapmle/255_paper_impedance_data.csv", encoding='latin1')
data16 = pd.read_csv("Data/P2_26.08.2025/06.09.2025/NEW_Sample/255_paper_impedance_data.csv", encoding='latin1')

x = data6['Freq'].values

# Impedance values
impedance_data = [
    data6['Impedance'].values, data7['Impedance'], data3['Impedance'].values,
    data16['Impedance'].values, data8['Impedance'].values
]

# Labels 
labels = [
    '118 6new', '118 2new', '118 2old', '255new', '255 old'
]

# Normalization function
def normalize(data):
    min_val = min(data)
    max_val = max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

# Normalize each dataset
normalized_data = [normalize(y) for y in impedance_data]

# Plot normalized data
plt.figure(figsize=(12, 8))

for i, y_norm in enumerate(normalized_data):
    plt.plot(x, y_norm, label=f'Sample {labels[i]}', marker='o', markersize=4, linestyle='-')

# Adding labels and legend
plt.title('Min-Max Normalized Impedance Data', fontsize=16)
plt.xlabel('Frequency (Hz)', fontsize=14)
plt.ylabel('Normalized Impedance', fontsize=14)
plt.legend(fontsize=10, title="Samples")
plt.grid()

# Show the plot
plt.tight_layout()
plt.show()
