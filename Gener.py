import csv
import pandas as pd
import matplotlib.pyplot as plt

# Read CSV data
data = pd.read_csv('data.csv')
pressure = data['pressure']
voltage = data['voltage']

# Write data to TXT file
with open('data.txt', 'w') as txt_file:
    writer = csv.writer(txt_file, delimiter='\t')
    writer.writerows(zip(pressure, voltage))

# Create scatter plot
plt.scatter(pressure, voltage, color='C3')
plt.xlabel('Pressure')
plt.ylabel('Voltage')
plt.title('Scatter Plot')
plt.tight_layout()

# Save plot as PNG file
plt.savefig('scatter_plot.png')

# Display the plot
plt.show()