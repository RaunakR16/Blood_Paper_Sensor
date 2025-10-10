import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Read data
data1 = pd.read_csv("10khz.csv", encoding='latin1')

x = data1['Number'].values
y1 = data1['Value'].values

# Average every 10 consecutive values
n = 10
y1_avg = [np.mean(y1[i:i+n]) for i in range(0, len(y1), n)]

# For x, take the midpoint (or first value) of each group of 10 points
x_avg = [np.mean(x[i:i+n]) for i in range(0, len(x), n)]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x_avg, y1_avg, label='Averaged Data', color='orange', markersize=4)

# Adding labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Time Vs frequency (Khz)')
plt.legend()
plt.grid(True)

# Show plot
plt.tight_layout()
plt.show()
