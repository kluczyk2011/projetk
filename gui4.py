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
import multiprocessing as mp
import os
import Symulator_zbieracza_danych
from threading import Thread
import threading
import sys
import Wykres_rzecz
import Generi


def start_process():
    # Start the animation in a separate thread
    animation_thread = Thread(target=Wykres_rzecz.run_animation)
    animation_thread.start()

    # Start logging data in a separate thread
    data_logger_thread = Thread(target=Symulator_zbieracza_danych.log_data)
    data_logger_thread.start()


def koniec():
    Symulator_zbieracza_danych.running = False
    Wykres_rzecz.terminated = True
    sys.exit()


def save_csv_data():
    # Get the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Get the folder name and file name from the Entry widgets
    folder_name = folder_entry.get()
    file_name = file_entry.get()

    # Create the folder path inside the script's directory
    folder_path = os.path.join(script_dir, folder_name)

    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Create the file path inside the folder
    file_path = os.path.join(folder_path, file_name)

    # Save the data as a CSV file
    data = pd.read_csv('data.csv')
    data.to_csv(file_path, index=False)

    print(f"CSV file '{file_path}' saved successfully")


# Create the main window
window = tk.Tk()
window.title("GUI Example")

# Create a button to start the process
start_button = tk.Button(window, text="Start Process", command=start_process)
start_button.pack()

exit_button = tk.Button(window, text="Stop", command=koniec)
exit_button.pack()

generuj_button = tk.Button(window, text="Generuj", command=Generi.genero)
generuj_button.pack()

zapis_button = tk.Button(window, text="Zapisz CSV", command=save_csv_data)
zapis_button.pack()

# Create Entry widgets for folder name and file name
folder_entry = tk.Entry(window)
folder_entry.pack()

file_entry = tk.Entry(window)
file_entry.pack()

# Start the GUI main loop
window.mainloop()

