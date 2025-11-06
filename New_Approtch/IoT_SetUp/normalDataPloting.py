import matplotlib.pyplot as plt
#import numpy as np
import pandas as pd

# Use consistent forward slashes

data1 = pd.read_csv("10khz.csv", encoding='latin1')

x = data1['Number'].values

y1 = data1['Value'].values

# Plotting
plt.figure(figsize=(10, 6))


plt.plot(x, y1, label='data', color='orange', markersize=4)


# Adding labels and title
plt.xlabel('Frequency (Hz)')
plt.ylabel('Impedance')
plt.title('Impedance vs Frequency')
plt.legend()
plt.grid(True)

# Show plot
plt.tight_layout()
plt.show()
