import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Data
data1 = pd.read_csv("Data\P2_26.08.2025/26.08.2025/105_impedance_data.csv", encoding='latin1')
data2 = pd.read_csv("Data/P2_26.08.2025/26.08.2025/110_impedance_data.csv", encoding='latin1')
data3 = pd.read_csv("Data/P2_26.08.2025/26.08.2025/112_impedance_data.csv", encoding='latin1')
data4 = pd.read_csv("Data/P2_26.08.2025/26.08.2025/115_impedance_data.csv", encoding='latin1')
data5 = pd.read_csv("Data/P2_26.08.2025/26.08.2025/119_impedance_data.csv", encoding='latin1')
data6 = pd.read_csv("Data/P2_26.08.2025/26.08.2025/121_impedance_data.csv", encoding='latin1')
data7 = pd.read_csv("Data/P2_26.08.2025/26.08.2025/148_impedance_data.csv", encoding='latin1')
data8 = pd.read_csv("Data/P2_26.08.2025/26.08.2025/177_impedance_data.csv", encoding='latin1')
data9 = pd.read_csv("Data\P2_26.08.2025/26.08.2025/343_paper_impedance_data.csv", encoding='latin1')
data10 = pd.read_csv("Data/P2_26.08.2025/26.08.2025/484_impedance_data.csv", encoding='latin1')

x = data1['Freq'].values

# Impedance values
impedance_data = [
    data1['Impedance'].values, data2['Impedance'].values, data3['Impedance'].values,
    data4['Impedance'].values, data5['Impedance'].values, data6['Impedance'].values,
    data7['Impedance'].values, data9['Impedance'].values,
    data10['Impedance'].values
]

# Labels corresponding to the CSV file numbers
labels = [
    '105', '110', '112', '115', '119', '121', '148', '343', '484'
]

# Perform FFT and plot results
plt.figure(figsize=(12, 8))

for i, y in enumerate(impedance_data):
    fft_y = np.fft.fft(y)  
    frequencies = np.fft.fftfreq(len(y))  
    magnitude = np.abs(fft_y) 
    plt.plot(frequencies[:len(frequencies)//2], magnitude[:len(magnitude)//2], label=labels[i], linestyle='-', marker='o', markersize=4)

plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.title('FFT of Impedance Data')
plt.legend(title="Sample Numbers", loc='upper right', fontsize='small')
plt.grid(True)
plt.tight_layout()

plt.show()
