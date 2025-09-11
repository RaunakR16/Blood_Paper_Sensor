import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Use consistent forward slashes
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

print(data1.head())
print(data2.head())
print(data3.head())
print(data4.head())
print(data5.head())
print(data6.head())
print(data7.head())
print(data9.head())
print(data10.head())
print(data11.head())


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
y11 = data11['Impedance'].values

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='66', color='blue', linestyle='-', marker='o', markersize=4)
plt.plot(x, y2, label='70', color='red', linestyle='-', marker='o', markersize=4)
plt.plot(x, y3, label='73', color='green', linestyle='-', marker='o', markersize=4)
plt.plot(x, y4, label='81', color='pink', linestyle='-', marker='o', markersize=4)
plt.plot(x, y5, label='104', color='orange', linestyle='-', marker='o', markersize=4)
plt.plot(x, y6, label='111', color='purple', linestyle='-', marker='o', markersize=4)
plt.plot(x, y7, label='118', color='brown', linestyle='-', marker='o', markersize=4)
plt.plot(x, y9, label='136', color='cyan', linestyle='-', marker='o', markersize=4)
plt.plot(x, y10, label='228', color='magenta', linestyle='-', marker='o', markersize=4)
plt.plot(x, y11, label='252', color='yellow', linestyle='-', marker='o', markersize=4)

# Adding labels and title
plt.xlabel('Frequency (Hz)')
plt.ylabel('Impedance')
plt.title('Impedance vs Frequency')
plt.legend()
plt.grid(True)

# Show plot
plt.tight_layout()
plt.show()
