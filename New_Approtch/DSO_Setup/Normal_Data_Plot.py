import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Use consistent forward slashes
data1 = pd.read_csv("data06-11-2025\SDS00003.CSV", encoding='latin1')

print(data1.head())

y1 = data1['Volt'].values


# Plotting
plt.figure(figsize=(10, 6))
plt.plot( y1, label='NaCl', color='blue', linestyle='-', markersize=4)


# Adding labels and title
plt.xlabel('Time (mS)')
plt.ylabel('Voltage (volt)')
plt.title('Time Vs Voltage')
plt.legend()
plt.grid(True)

# Show plot
plt.tight_layout()
plt.show()