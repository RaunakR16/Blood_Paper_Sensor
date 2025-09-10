import matplotlib.pyplot as plt
from scipy.stats import kurtosis, skew
import pandas as pd

# Data
data1 = pd.read_csv("Data/P2_26.08.2025/06.09.2025/OLD_Sapmle/88_paper_impedance_data.csv", encoding='latin1')
data2 = pd.read_csv("Data\P2_26.08.2025/06.09.2025/OLD_Sapmle/99_paper_impedance_data.csv", encoding='latin1')
data3 = pd.read_csv("Data\P2_26.08.2025/06.09.2025/OLD_Sapmle/132_paper_impedance_data.csv", encoding='latin1')
data4 = pd.read_csv("Data\P2_26.08.2025/06.09.2025/OLD_Sapmle/139_paper_impedance_data.csv", encoding='latin1')
data5 = pd.read_csv("Data\P2_26.08.2025/06.09.2025/OLD_Sapmle/139b_paper_impedance_data.csv", encoding='latin1')
data6 = pd.read_csv("Data\P2_26.08.2025/06.09.2025/OLD_Sapmle/181_paper_impedance_data.csv", encoding='latin1')
data7 = pd.read_csv("Data\P2_26.08.2025/06.09.2025/OLD_Sapmle/220_paper_impedance_data.csv", encoding='latin1')
data8 = pd.read_csv("Data\P2_26.08.2025/06.09.2025/OLD_Sapmle/255_paper_impedance_data.csv", encoding='latin1')

# Impedance values
impedance_data = [
    data1['Impedance'].values, data2['Impedance'].values, data3['Impedance'].values,
    data4['Impedance'].values, data5['Impedance'].values, data6['Impedance'].values,
    data7['Impedance'].values, data8['Impedance'].values
]

# Labels for datasets
labels = [
    '88', '99', '132', '139', '139b', '181', '220', '255'
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
