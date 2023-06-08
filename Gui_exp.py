import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import subprocess

# Function to start the process
def start_process():
    # Run the script with subprocess
    subprocess.Popen(["python", r"C:\Users\Doge\Desktop\projekt od wjerzana\Symulator_zbieracza_danych.py"])
    subprocess.Popen(["python", r"C:\Users\Doge\Desktop\projekt od wjerzana\Wykres_rzecz.py"])

    
# Create the main window
window = tk.Tk()
window.title("GUI Example")

# Create a button to start the process
start_button = tk.Button(window, text="Start Process", command=start_process)
start_button.pack()

# Create a window for the plot
fig = Figure(figsize=(5, 4), dpi=100)
plot_window = FigureCanvasTkAgg(fig, master=window)
plot_window.get_tk_widget().pack()

# Function to update the plot
def update_plot():
    # Add your code to update the plot here
    # You can access the plot data from the other script and update the figure accordingly
    # For example, you can use fig.add_subplot() and plot your data

    # Call this function again after a certain interval
    fig.clear()
    window.after(1000, update_plot)  # Update every 1 second

# Start updating the plot
update_plot()

# Start the GUI main loop
window.mainloop()
