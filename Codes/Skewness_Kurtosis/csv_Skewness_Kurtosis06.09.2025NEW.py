import matplotlib.pyplot as plt
from scipy.stats import kurtosis, skew
import pandas as pd

# Data
data1 = pd.read_csv("Data/P2_26.08.2025/06.09.2025/NEW_Sample/76_paper_impedance_data.csv", encoding='latin1')
data2 = pd.read_csv("Data/P2_26.08.2025/06.09.2025/NEW_Sample/81_paper_impedance_data.csv", encoding='latin1')
data3 = pd.read_csv("Data/P2_26.08.2025/06.09.2025/NEW_Sample/88_paper_impedance_data.csv", encoding='latin1')
data4 = pd.read_csv("Data/P2_26.08.2025/06.09.2025/NEW_Sample/93_paper_impedance_data.csv", encoding='latin1')
data5 = pd.read_csv("Data/P2_26.08.2025/06.09.2025/NEW_Sample/115_paper_impedance_data.csv", encoding='latin1')
data6 = pd.read_csv("Data/P2_26.08.2025/06.09.2025/NEW_Sample/118_paper_impedance_data.csv", encoding='latin1')
data7 = pd.read_csv("Data/P2_26.08.2025/06.09.2025/NEW_Sample/119_paper_impedance_data.csv", encoding='latin1')
data8 = pd.read_csv("Data/P2_26.08.2025/06.09.2025/NEW_Sample/124_paper_impedance_data.csv", encoding='latin1')
data9 = pd.read_csv("Data/P2_26.08.2025/06.09.2025/NEW_Sample/140_paper_impedance_data.csv", encoding='latin1')
data10 = pd.read_csv("Data/P2_26.08.2025/06.09.2025/NEW_Sample/150_paper_impedance_data.csv", encoding='latin1')
data11 = pd.read_csv("Data/P2_26.08.2025/06.09.2025/NEW_Sample/157_paper_impedance_data.csv", encoding='latin1')
data12 = pd.read_csv("Data/P2_26.08.2025/06.09.2025/NEW_Sample/168_paper_impedance_data.csv", encoding='latin1')
data13 = pd.read_csv("Data/P2_26.08.2025/06.09.2025/NEW_Sample/170_paper_impedance_data.csv", encoding='latin1')
data14 = pd.read_csv("Data/P2_26.08.2025/06.09.2025/NEW_Sample/180_paper_impedance_data.csv", encoding='latin1')    
data15 = pd.read_csv("Data/P2_26.08.2025/06.09.2025/NEW_Sample/240_paper_impedance_data.csv", encoding='latin1')
data16 = pd.read_csv("Data/P2_26.08.2025/06.09.2025/NEW_Sample/255_paper_impedance_data.csv", encoding='latin1')
data17 = pd.read_csv("Data/P2_26.08.2025/06.09.2025/NEW_Sample/273_paper_impedance_data.csv", encoding='latin1')
data18 = pd.read_csv("Data/P2_26.08.2025/06.09.2025/NEW_Sample/275_paper_impedance_data.csv", encoding='latin1')

# Impedance values
impedance_data = [
    data1['Impedance'].values, data2['Impedance'].values, data3['Impedance'].values,
    data4['Impedance'].values, data5['Impedance'].values, data6['Impedance'].values,
    data7['Impedance'].values, data8['Impedance'].values, data9['Impedance'].values,
    data10['Impedance'].values, data11['Impedance'].values, data12['Impedance'].values,
    data13['Impedance'].values, data14['Impedance'].values, data15['Impedance'].values,
    data16['Impedance'].values, data17['Impedance'].values, data18['Impedance'].values
]

# Labels for datasets
labels = [
    '76', '81', '88', '93', '115', '118', '119', '124', '140', '150',
    '157', '168', '170', '180', '240', '255', '273', '275'
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
