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
# Create four spaces for writing
nazwa = tk.Entry(window)
nazwa.pack()

text_entry2 = tk.Entry(window)
text_entry2.pack()

text_entry3 = tk.Entry(window)
text_entry3.pack()

text_entry4 = tk.Entry(window)
text_entry4.pack()

# Start the GUI main loop
window.mainloop()