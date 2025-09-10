import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Use consistent forward slashes
data1 = pd.read_csv("Data/P2_26.08.2025/02.09.2025\OLD_Sample/76_paper_impedance_data.csv", encoding='latin1')
data2 = pd.read_csv("Data/P2_26.08.2025/02.09.2025\OLD_Sample/96_paper_impedance_data.csv", encoding='latin1')
data3 = pd.read_csv("Data/P2_26.08.2025/02.09.2025\OLD_Sample/97_paper_impedance_data.csv", encoding='latin1')
data4 = pd.read_csv("Data/P2_26.08.2025/02.09.2025\OLD_Sample/100_paper_impedance_data.csv", encoding='latin1')
data5 = pd.read_csv("Data/P2_26.08.2025/02.09.2025\OLD_Sample/108_paper_impedance_data.csv", encoding='latin1')
data6 = pd.read_csv("Data/P2_26.08.2025/02.09.2025\OLD_Sample/117_paper_impedance_data.csv", encoding='latin1')
data7 = pd.read_csv("Data/P2_26.08.2025/02.09.2025\OLD_Sample/118_paper_impedance_data.csv", encoding='latin1')
data8 = pd.read_csv("Data/P2_26.08.2025/02.09.2025\OLD_Sample/148_paper_impedance_data.csv", encoding='latin1')
data9 = pd.read_csv("Data/P2_26.08.2025/02.09.2025\OLD_Sample/168_paper_impedance_data.csv", encoding='latin1')
data10 = pd.read_csv("Data/P2_26.08.2025/02.09.2025\OLD_Sample/170_paper_impedance_data.csv", encoding='latin1')
data11 = pd.read_csv("Data/P2_26.08.2025/02.09.2025\OLD_Sample/187_paper_impedance_data.csv", encoding='latin1')
data12 = pd.read_csv("Data/P2_26.08.2025/02.09.2025\OLD_Sample/188_paper_impedance_data.csv", encoding='latin1')
data13 = pd.read_csv("Data/P2_26.08.2025/02.09.2025\OLD_Sample/188_b_paper_impedance_data.csv", encoding='latin1')
data14 = pd.read_csv("Data/P2_26.08.2025/02.09.2025\OLD_Sample/309_paper_impedance_data.csv", encoding='latin1')    
data15 = pd.read_csv("Data/P2_26.08.2025/02.09.2025\OLD_Sample/487_paper_impedance_data.csv", encoding='latin1')

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
print(data12.head())
print(data13.head())
print(data14.head())
print(data15.head())



x = data1['Freq'].values

y1 = data1['Impedance'].values
y2 = data2['Impedance'].values
y3 = data3['Impedance'].values
y4 = data4['Impedance'].values
y5 = data5['Impedance'].values
y6 = data6['Impedance'].values
y7 = data7['Impedance'].values
y8 = data8['Impedance'].values
y9 = data9['Impedance'].values
y10 = data10['Impedance'].values
y11 = data11['Impedance'].values
y12 = data12['Impedance'].values
y13 = data13['Impedance'].values
y14 = data14['Impedance'].values
y15 = data15['Impedance'].values

# Plotting
plt.figure(figsize=(10, 6))

plt.plot(x, y1, label='76', color='blue', linestyle='-', marker='o', markersize=4)
plt.plot(x, y2, label='96', color='red', linestyle='-', marker='o', markersize=4)
plt.plot(x, y3, label='97', color='green', linestyle='-', marker='o', markersize=4)
plt.plot(x, y4, label='100', color='pink', linestyle='-', marker='o', markersize=4)
plt.plot(x, y5, label='108', color='orange', linestyle='-', marker='o', markersize=4)
plt.plot(x, y6, label='117', color='purple', linestyle='-', marker='o', markersize=4)
plt.plot(x, y7, label='118', color='brown', linestyle='-', marker='o', markersize=4)
plt.plot(x, y8, label='148', color='cyan', linestyle='-', marker='o', markersize=4)
plt.plot(x, y9, label='168', color='magenta', linestyle='-', marker='o', markersize=4)
plt.plot(x, y10, label='170', color='yellow', linestyle='-', marker='o', markersize=4)
plt.plot(x, y11, label='187', color='grey', linestyle='-', marker='o', markersize=4)
plt.plot(x, y12, label='188', color='olive', linestyle='-', marker  ='o', markersize=4)
plt.plot(x, y13, label='188_b', color='teal', linestyle='-', marker='o', markersize=4)
plt.plot(x, y14, label='309', color='navy', linestyle='-', marker='o', markersize=4)
plt.plot(x, y15, label='487', color='lime', linestyle='-', marker='o', markersize=4)

# Adding labels and title
plt.xlabel('Frequency (Hz)')
plt.ylabel('Impedance')
plt.title('Impedance vs Frequency')
plt.legend()
plt.grid(True)

# Show plot
plt.tight_layout()
plt.show()
