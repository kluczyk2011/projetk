
import csv
import pandas as pd
import matplotlib as plt

with open('data.csv', 'r') as data_in, open('data.txt', 'w') as txt_out:
    zaw = data_in.read()
    txt_out.write(zaw)

#czytam csv i robie z niego wykres w png do zapisania
data= pd.read_csv('data.csv')
pressure=data['pressure']
voltage = data['voltage']

plt.scatter(pressure, voltage, color='C3',)
plt.legend()
plt.tight_layout()
plt.savefig("wykres.pdf")
plt.show()