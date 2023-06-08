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


pressure_dat = []

index = count()

def animate(i):
    
    data =  pd.read_csv('data.csv')
    pressure_dat= data['pressure']
    voltage_dat = data['voltage']
    
    plt.cla()

    plt.plot(pressure_dat, voltage_dat)
    plt.legend(loc='upper right')
    plt.tight_layout()



ani = FuncAnimation(plt.gcf(), animate, interval=500)
plt.tight_layout()
plt.show()

