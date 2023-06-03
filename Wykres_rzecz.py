import numpy as np
import random as rnd
import time
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
import pandas as pd

voltage= []
pressure = []

index = count()

def animate(i):
    data =  pd.read_csv('data.csv')
    pressure= data['pressure']
    voltage = data['voltage']
    
    plt.cla()

    plt.plot(pressure, voltage)
    plt.legend(loc='upper right')
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval=1000)
plt.tight_layout()
plt.show()

