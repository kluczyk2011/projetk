import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import subprocess
import numpy as np
import random as rnd
import time
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
import pandas as pd
import subprocess
import multiprocessing

subprocesses = []

def start_process():
    # Run the script with subprocess
    subprocesses.append(subprocess.Popen(["python", r"C:\Users\Doge\Desktop\projekt od wjerzana\Zbieracz_mik.py"]))
    subprocesses.append(subprocess.Popen(["python", r"C:\Users\Doge\Desktop\projekt od wjerzana\Wykres_rzecz.py"]))

def koniec():
    for process in subprocesses:
        process.terminate()
    exit()

def gener():
    subprocesses.append(subprocess.Popen(["python",r"C:\Users\Doge\Desktop\projekt od wjerzana\Gener.py"]))

##############################################
##########################################

def save_csv_data(data, folder_name, file_name):
    # Get the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Create the folder path inside the script's directory
    folder_path = os.path.join(script_dir, folder_name)
    
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # Create the file path inside the folder
    file_path = os.path.join(folder_path, file_name)
    
    # Save the data as a CSV file
   
    
    data = pd.read_csv('data.csv')
    pressure = data['pressure']
    voltage = data['voltage']

    fieldnames= ["pressure", "voltage"]
    with open(file_path, 'w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerrows(data)
    
    print(f"CSV file '{file_path}' saved successfully")

##################################################
#####################################


# Create the main window
window = tk.Tk()
window.title("GUI Example")

# Create a button to start the process
start_button = tk.Button(window, text="Start Process", command=start_process)
start_button.pack()

exit_button = tk.Button(window, text="stop", command=koniec)
exit_button.pack()

Generuj_button = tk.Button(window, text="Generuj", command=gener)
Generuj_button.pack()

zapis_button = tk.Button(window, text="zapis", command=save_csv_data)
zapis_button.pack()

# Create four spaces for writing
file_name = tk.Entry(window)
file_name.pack()

folder_name = tk.Entry(window)
folder_name.pack()

text_entry3 = tk.Entry(window)
text_entry3.pack()

text_entry4 = tk.Entry(window)
text_entry4.pack()

# Start the GUI main loop
window.mainloop()