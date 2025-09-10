import matplotlib.pyplot as plt
from scipy.stats import kurtosis, skew
import pandas as pd

# Data
data1 = pd.read_csv("C:/Users/rauna/Downloads/Blood_Paper_Sensor/Data/P2_26.08.2025/02.09.2025/NEW_Sample/66_paper_impedance_data.csv", encoding='latin1')
data2 = pd.read_csv("C:/Users/rauna/Downloads/Blood_Paper_Sensor/Data/P2_26.08.2025/02.09.2025/NEW_Sample/70_paper_impedance_data.csv", encoding='latin1')
data3 = pd.read_csv("C:/Users/rauna/Downloads/Blood_Paper_Sensor/Data/P2_26.08.2025/02.09.2025/NEW_Sample/73_paper_impedance_data.csv", encoding='latin1')
data4 = pd.read_csv("C:/Users/rauna/Downloads/Blood_Paper_Sensor/Data/P2_26.08.2025/02.09.2025/NEW_Sample/81_paper_impedance_data.csv", encoding='latin1')
data5 = pd.read_csv("C:/Users/rauna/Downloads/Blood_Paper_Sensor/Data/P2_26.08.2025/02.09.2025/NEW_Sample/104_paper_impedance_data.csv", encoding='latin1')
data6 = pd.read_csv("C:/Users/rauna/Downloads/Blood_Paper_Sensor/Data/P2_26.08.2025/02.09.2025/NEW_Sample/111_paper_impedance_data.csv", encoding='latin1')
data7 = pd.read_csv("C:/Users/rauna/Downloads/Blood_Paper_Sensor/Data/P2_26.08.2025/02.09.2025/NEW_Sample/118_paper_impedance_data.csv", encoding='latin1')
data8 = pd.read_csv("C:/Users/rauna/Downloads/Blood_Paper_Sensor/Data/P2_26.08.2025/02.09.2025/NEW_Sample/136_paper_impedance_data.csv", encoding='latin1')
data9 = pd.read_csv("C:/Users/rauna/Downloads/Blood_Paper_Sensor/Data/P2_26.08.2025/02.09.2025/NEW_Sample/228_paper_impedance_data.csv", encoding='latin1')
data10 = pd.read_csv("C:/Users/rauna/Downloads/Blood_Paper_Sensor/Data/P2_26.08.2025/02.09.2025/NEW_Sample/252_paper_impedance_data.csv", encoding='latin1')

# Impedance values
impedance_data = [
    data1['Impedance'].values, data2['Impedance'].values, data3['Impedance'].values,
    data4['Impedance'].values, data5['Impedance'].values, data6['Impedance'].values,
    data7['Impedance'].values, data8['Impedance'].values, data9['Impedance'].values,
    data10['Impedance'].values
]

# Labels for datasets
labels = [
    '66', '70', '73', '81', '104', '111', '118', '136', '228', '252'
]

# Compute skewness and kurtosis
skewness_values = [skew(data) for data in impedance_data]
kurtosis_values = [kurtosis(data) for data in impedance_data]

# Bar Graph Plot
x = range(len(labels))  # Positions for the bars

fig, ax = plt.subplots(figsize=(12, 8))

# Plotting skewness
ax.bar([pos - 0.2 for pos in x], skewness_values, width=0.4, label='Skewness', color='blue')

# Plotting kurtosis
ax.bar([pos + 0.2 for pos in x], kurtosis_values, width=0.4, label='Kurtosis', color='orange')

# Adding labels and legend
ax.set_xlabel('Datasets', fontsize=14)
ax.set_ylabel('Values', fontsize=14)
ax.set_title('Skewness and Kurtosis for Different Datasets', fontsize=16)
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=12, rotation=45)
ax.legend(fontsize=12)

# Show the plot
plt.tight_layout()
plt.show()
