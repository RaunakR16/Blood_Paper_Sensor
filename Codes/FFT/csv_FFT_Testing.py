import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Data
# data1 = pd.read_csv("Data\P2_26.08.2025/26.08.2025/105_impedance_data.csv", encoding='latin1')
# data2 = pd.read_csv("Data/P2_26.08.2025/26.08.2025/110_impedance_data.csv", encoding='latin1')
# data3 = pd.read_csv("Data/P2_26.08.2025/26.08.2025/112_impedance_data.csv", encoding='latin1')
# data4 = pd.read_csv("Data/P2_26.08.2025/26.08.2025/115_impedance_data.csv", encoding='latin1')
# data5 = pd.read_csv("Data/P2_26.08.2025/26.08.2025/119_impedance_data.csv", encoding='latin1')
# data6 = pd.read_csv("Data/P2_26.08.2025/26.08.2025/121_impedance_data.csv", encoding='latin1')
# data7 = pd.read_csv("Data/P2_26.08.2025/26.08.2025/148_impedance_data.csv", encoding='latin1')
# data8 = pd.read_csv("Data/P2_26.08.2025/26.08.2025/177_impedance_data.csv", encoding='latin1')
# data9 = pd.read_csv("Data\P2_26.08.2025/26.08.2025/343_paper_impedance_data.csv", encoding='latin1')
# data10 = pd.read_csv("Data/P2_26.08.2025/26.08.2025/484_impedance_data.csv", encoding='latin1')
#data5 = pd.read_csv("Data/P2_26.08.2025/06.09.2025/NEW_Sample/115_paper_impedance_data.csv", encoding='latin1')
data6 = pd.read_csv("Data/P2_26.08.2025/06.09.2025/NEW_Sample/118_paper_impedance_data.csv", encoding='latin1')
data7 = pd.read_csv("C:/Users/rauna/Downloads/Blood_Paper_Sensor/Data/P2_26.08.2025/02.09.2025/NEW_Sample/118_paper_impedance_data.csv", encoding='latin1')
data8 = pd.read_csv("Data/P2_26.08.2025/02.09.2025\OLD_Sample/118_paper_impedance_data.csv", encoding='latin1')
data9 = pd.read_csv("Data/P2_26.08.2025/06.09.2025/NEW_Sample/119_paper_impedance_data.csv", encoding='latin1')
data18 = pd.read_csv("Data/P2_26.08.2025/06.09.2025/NEW_Sample/275_paper_impedance_data.csv", encoding='latin1')

x = data6['Freq'].values

# Impedance values
impedance_data = [
    data6['Impedance'].values, data7['Impedance'].values, data8['Impedance'].values, data9['Impedance'].values, data18['Impedance'].values

]


# Labels corresponding to the CSV file numbers
labels = [
    '118 6new', '118 2new', '118 2OLD', '119 6new', '275 6new'
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
