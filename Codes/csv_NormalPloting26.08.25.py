import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Use consistent forward slashes
# Use raw strings for file paths
data1 = pd.read_csv("Data\P2_26.08.2025/26.08.2025/105_impedance_data.csv", encoding='latin1')
data2 = pd.read_csv("Data/P2_26.08.2025/26.08.2025/110_impedance_data.csv", encoding='latin1')
data3 = pd.read_csv("Data/P2_26.08.2025/26.08.2025/112_impedance_data.csv", encoding='latin1')
data4 = pd.read_csv("Data/P2_26.08.2025/26.08.2025/115_impedance_data.csv", encoding='latin1')
data5 = pd.read_csv("Data/P2_26.08.2025/26.08.2025/119_impedance_data.csv", encoding='latin1')
data6 = pd.read_csv("Data/P2_26.08.2025/26.08.2025/121_impedance_data.csv", encoding='latin1')
data7 = pd.read_csv("Data/P2_26.08.2025/26.08.2025/148_impedance_data.csv", encoding='latin1')
data9 = pd.read_csv("Data/P2_26.08.2025/26.08.2025/177_impedance_data.csv", encoding='latin1')
data10 = pd.read_csv("Data/P2_26.08.2025/26.08.2025/484_impedance_data.csv", encoding='latin1')

print(data1.head())
print(data2.head())
print(data3.head())
print(data4.head())
print(data5.head())
print(data6.head())
print(data7.head())
print(data9.head())
print(data10.head())



x = data1['Freq'].values

y1 = data1['Impedance'].values
y2 = data2['Impedance'].values
y3 = data3['Impedance'].values
y4 = data4['Impedance'].values
y5 = data5['Impedance'].values
y6 = data6['Impedance'].values
y7 = data7['Impedance'].values
y9 = data9['Impedance'].values
y10 = data10['Impedance'].values


# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='105', color='blue', linestyle='-', marker='o', markersize=4)
plt.plot(x, y2, label='110', color='red', linestyle='-', marker='o', markersize=4)
plt.plot(x, y3, label='112', color='green', linestyle='-', marker='o', markersize=4)
plt.plot(x, y4, label='119', color='pink', linestyle='-', marker='o', markersize=4)
plt.plot(x, y5, label='121', color='orange', linestyle='-', marker='o', markersize=4)
plt.plot(x, y6, label='148', color='purple', linestyle='-', marker='o', markersize=4)
plt.plot(x, y7, label='177', color='brown', linestyle='-', marker='o', markersize=4)
plt.plot(x, y9, label='343', color='cyan', linestyle='-', marker='o', markersize=4)
plt.plot(x, y10, label='484', color='magenta', linestyle='-', marker='o', markersize=4)


# Adding labels and title
plt.xlabel('Frequency (Hz)')
plt.ylabel('Impedance')
plt.title('Impedance vs Frequency')
plt.legend()
plt.grid(True)

# Show plot
plt.tight_layout()
plt.show()
