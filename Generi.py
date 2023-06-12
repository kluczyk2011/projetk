import csv
import pandas as pd
import matplotlib.pyplot as plt

def genero():
    # Read CSV data
    data = pd.read_csv('data.csv')
    pressure = data['pressure']
    voltage = data['voltage']

    # Write data to TXT file
    with open('data.txt', 'w') as txt_file:
        writer = csv.writer(txt_file, delimiter='\t')
        writer.writerows(zip(pressure, voltage))

    # Create scatter plot
    fig, ax = plt.subplots()
    scatter = ax.scatter(pressure, voltage, color='C3')
    ax.set_xlabel('Pressure')
    ax.set_ylabel('Voltage')
    ax.set_title('Scatter Plot')
    plt.tight_layout()

    # Save plot as PNG file
    plt.savefig('scatter_plot.png')
    plt.show()
