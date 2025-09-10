import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Use consistent forward slashes

data6 = pd.read_csv("Data/P2_26.08.2025/06.09.2025/NEW_Sample/118_paper_impedance_data.csv", encoding='latin1')

data7 = pd.read_csv("C:/Users/rauna/Downloads/Blood_Paper_Sensor/Data/P2_26.08.2025/02.09.2025/NEW_Sample/118_paper_impedance_data.csv", encoding='latin1')

data8 = pd.read_csv("Data/P2_26.08.2025/02.09.2025\OLD_Sample/118_paper_impedance_data.csv", encoding='latin1')

# print(data1.head())
# print(data2.head())
# print(data3.head())
# print(data4.head())
# print(data5.head())
# print(data6.head())
# print(data7.head())
# print(data9.head())
# print(data10.head())
# print(data11.head())
# print(data12.head())
# print(data13.head())
# print(data14.head())
# print(data15.head())
# print(data16.head())
# print(data17.head())
# print(data18.head())



x = data6['Freq'].values

# y1 = data1['Impedance'].values
# y2 = data2['Impedance'].values
# y3 = data3['Impedance'].values
# y4 = data4['Impedance'].values
# y5 = data5['Impedance'].values
y6 = data6['Impedance'].values
y7 = data7['Impedance'].values
y8 = data8['Impedance'].values
# y9 = data9['Impedance'].values
# y10 = data10['Impedance'].values
# y11 = data11['Impedance'].values
# y12 = data12['Impedance'].values
# y13 = data13['Impedance'].values
# y14 = data14['Impedance'].values
# y15 = data15['Impedance'].values
# y16 = data16['Impedance'].values
# y17 = data17['Impedance'].values
# y18 = data18['Impedance'].values

# Plotting
plt.figure(figsize=(10, 6))


plt.plot(x, y6, label='118', color='orange', linestyle='-', marker='o', markersize=4)

plt.plot(x, y7, label='118', color='blue', linestyle='-', marker='o', markersize=4)

plt.plot(x, y8, label='118', color='red', linestyle='-', marker='o', markersize=4)

# Adding labels and title
plt.xlabel('Frequency (Hz)')
plt.ylabel('Impedance')
plt.title('Impedance vs Frequency')
plt.legend()
plt.grid(True)

# Show plot
plt.tight_layout()
plt.show()
