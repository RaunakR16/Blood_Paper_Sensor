import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Corrected file paths with consistent forward slashes
data1 = pd.read_csv("Data/P2_26.08.2025/06.09.2025/OLD_Sapmle/88_paper_impedance_data.csv", encoding='latin1')
data2 = pd.read_csv("Data/P2_26.08.2025/06.09.2025/OLD_Sapmle/99_paper_impedance_data.csv", encoding='latin1')
data3 = pd.read_csv("Data/P2_26.08.2025/06.09.2025/OLD_Sapmle/132_paper_impedance_data.csv", encoding='latin1')
data4 = pd.read_csv("Data/P2_26.08.2025/06.09.2025/OLD_Sapmle/139_paper_impedance_data.csv", encoding='latin1')
data5 = pd.read_csv("Data/P2_26.08.2025/06.09.2025/OLD_Sapmle/139b_paper_impedance_data.csv", encoding='latin1')
data6 = pd.read_csv("Data/P2_26.08.2025/06.09.2025/OLD_Sapmle/181_paper_impedance_data.csv", encoding='latin1')
data7 = pd.read_csv("Data/P2_26.08.2025/06.09.2025/OLD_Sapmle/220_paper_impedance_data.csv", encoding='latin1')
data8 = pd.read_csv("Data/P2_26.08.2025/06.09.2025/OLD_Sapmle/255_paper_impedance_data.csv", encoding='latin1')


print(data1.head())
print(data2.head())
print(data3.head())
print(data4.head())
print(data5.head())
print(data6.head())
print(data7.head())


x = data1['Freq'].values

y1 = data1['Impedance'].values
y2 = data2['Impedance'].values
y3 = data3['Impedance'].values
y4 = data4['Impedance'].values
y5 = data5['Impedance'].values
y6 = data6['Impedance'].values
y7 = data7['Impedance'].values
y8 = data8['Impedance'].values


# Plotting
plt.figure(figsize=(10, 6))

# plt.plot(x, y1, label='88', color='blue', linestyle='-', marker='o', markersize=4)
# plt.plot(x, y2, label='99', color='red', linestyle='-', marker='o', markersize=4)
# plt.plot(x, y3, label='132', color='green', linestyle='-', marker='o', markersize=4)
plt.plot(x, y4, label='139', color='pink', linestyle='-', marker='o', markersize=4)
plt.plot(x, y5, label='139b', color='orange', linestyle='-', marker='o', markersize=4)
# plt.plot(x, y6, label='181', color='purple', linestyle='-', marker='o', markersize=4)
# plt.plot(x, y7, label='220', color='brown', linestyle='-', marker='o', markersize=4)
# plt.plot(x, y8, label='255', color='cyan', linestyle='-', marker='o', markersize=4)


# Adding labels and title
plt.xlabel('Frequency (Hz)')
plt.ylabel('Impedance')
plt.title('Impedance vs Frequency')
plt.legend()
plt.grid(True)

# Show plot
plt.tight_layout()
plt.show()
