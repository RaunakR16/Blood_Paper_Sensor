import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Data
data1 = pd.read_csv("C:/Users/rauna/Downloads/Blood_Paper_Sensor/Data/P2_26.08.2025/02.09.2025/NEW_Sample/66_paper_impedance_data.csv", encoding='latin1')
data2 = pd.read_csv("C:/Users/rauna/Downloads/Blood_Paper_Sensor/Data/P2_26.08.2025/02.09.2025/NEW_Sample/70_paper_impedance_data.csv", encoding='latin1')
data3 = pd.read_csv("C:/Users/rauna/Downloads/Blood_Paper_Sensor/Data/P2_26.08.2025/02.09.2025/NEW_Sample/73_paper_impedance_data.csv", encoding='latin1')
data4 = pd.read_csv("C:/Users/rauna/Downloads/Blood_Paper_Sensor/Data/P2_26.08.2025/02.09.2025/NEW_Sample/81_paper_impedance_data.csv", encoding='latin1')
data5 = pd.read_csv("C:/Users/rauna/Downloads/Blood_Paper_Sensor/Data/P2_26.08.2025/02.09.2025/NEW_Sample/104_paper_impedance_data.csv", encoding='latin1')
data6 = pd.read_csv("C:/Users/rauna/Downloads/Blood_Paper_Sensor/Data/P2_26.08.2025/02.09.2025/NEW_Sample/111_paper_impedance_data.csv", encoding='latin1')
data7 = pd.read_csv("C:/Users/rauna/Downloads/Blood_Paper_Sensor/Data/P2_26.08.2025/02.09.2025/NEW_Sample/118_paper_impedance_data.csv", encoding='latin1')
data9 = pd.read_csv("C:/Users/rauna/Downloads/Blood_Paper_Sensor/Data/P2_26.08.2025/02.09.2025/NEW_Sample/136_paper_impedance_data.csv", encoding='latin1')
data10 = pd.read_csv("C:/Users/rauna/Downloads/Blood_Paper_Sensor/Data/P2_26.08.2025/02.09.2025/NEW_Sample/228_paper_impedance_data.csv", encoding='latin1')
data11 = pd.read_csv("C:/Users/rauna/Downloads/Blood_Paper_Sensor/Data/P2_26.08.2025/02.09.2025/NEW_Sample/252_paper_impedance_data.csv", encoding='latin1')

x = data1['Freq'].values

# Impedance values
impedance_data = [
    data1['Impedance'].values, data2['Impedance'].values, data3['Impedance'].values,
    data4['Impedance'].values, data5['Impedance'].values, data6['Impedance'].values,
    data7['Impedance'].values, data9['Impedance'].values,
    data10['Impedance'].values, data11['Impedance'].values
]

# Labels 
labels = [
    '66', '70', '73', '81', '104', '111', '118', '136', '228', '252'
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
