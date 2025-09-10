import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Data
data1 = pd.read_csv("Data/P2_26.08.2025/06.09.2025/OLD_Sapmle/88_paper_impedance_data.csv", encoding='latin1')
data2 = pd.read_csv("Data\P2_26.08.2025/06.09.2025/OLD_Sapmle/99_paper_impedance_data.csv", encoding='latin1')
data3 = pd.read_csv("Data\P2_26.08.2025/06.09.2025/OLD_Sapmle/132_paper_impedance_data.csv", encoding='latin1')
data4 = pd.read_csv("Data\P2_26.08.2025/06.09.2025/OLD_Sapmle/139_paper_impedance_data.csv", encoding='latin1')
data5 = pd.read_csv("Data\P2_26.08.2025/06.09.2025/OLD_Sapmle/139b_paper_impedance_data.csv", encoding='latin1')
data6 = pd.read_csv("Data\P2_26.08.2025/06.09.2025/OLD_Sapmle/181_paper_impedance_data.csv", encoding='latin1')
data7 = pd.read_csv("Data\P2_26.08.2025/06.09.2025/OLD_Sapmle/220_paper_impedance_data.csv", encoding='latin1')
data8 = pd.read_csv("Data\P2_26.08.2025/06.09.2025/OLD_Sapmle/255_paper_impedance_data.csv", encoding='latin1')

x = data1['Freq'].values

y1 = data1['Impedance'].values
y2 = data2['Impedance'].values
y3 = data3['Impedance'].values
y4 = data4['Impedance'].values
y5 = data5['Impedance'].values
y6 = data6['Impedance'].values
y7 = data7['Impedance'].values
y8 = data8['Impedance'].values

# Perform FFT
fft_y1 = np.fft.fft(y1)
fft_y2 = np.fft.fft(y2)
fft_y3 = np.fft.fft(y3)
fft_y4 = np.fft.fft(y4)
fft_y5 = np.fft.fft(y5)
fft_y6 = np.fft.fft(y6)
fft_y7 = np.fft.fft(y7)
fft_y8 = np.fft.fft(y8)

# Compute frequencies
frequencies = np.fft.fftfreq(len(y1))  

# Magnitude of FFT
magnitude_y1 = np.abs(fft_y1)
magnitude_y2 = np.abs(fft_y2)
magnitude_y3 = np.abs(fft_y3)
magnitude_y4 = np.abs(fft_y4)
magnitude_y5 = np.abs(fft_y5)
magnitude_y6 = np.abs(fft_y6)
magnitude_y7 = np.abs(fft_y7)
magnitude_y8 = np.abs(fft_y8)


# Plot FFT results
plt.figure(figsize=(12, 6))


plt.plot(frequencies[:len(frequencies)//2], magnitude_y1[:len(magnitude_y1)//2], label='88', color='blue', linestyle='-', marker='o', markersize=4)
plt.plot(frequencies[:len(frequencies)//2], magnitude_y2[:len(magnitude_y2)//2], label='99 ', color='red', linestyle='-', marker='o', markersize=4)
plt.plot(frequencies[:len(frequencies)//2], magnitude_y3[:len(magnitude_y3)//2], label='132', color='green', linestyle='-', marker='o', markersize=4)
plt.plot(frequencies[:len(frequencies)//2], magnitude_y4[:len(magnitude_y4)//2], label='139', color='purple', linestyle='-', marker='o', markersize=4)
plt.plot(frequencies[:len(frequencies)//2], magnitude_y5[:len(magnitude_y5)//2], label='139b', color='pink', linestyle='-', marker='o', markersize=4)
plt.plot(frequencies[:len(frequencies)//2], magnitude_y6[:len(magnitude_y6)//2], label='181', color='orange', linestyle='-', marker='o', markersize=4)
plt.plot(frequencies[:len(frequencies)//2], magnitude_y7[:len(magnitude_y7)//2], label='220', color='brown', linestyle='-', marker='o', markersize=4)
plt.plot(frequencies[:len(frequencies)//2], magnitude_y8[:len(magnitude_y8)//2], label='255', color='cyan', linestyle='-', marker='o', markersize=4)


plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.title('FFT of Blood Glucose Levels')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()