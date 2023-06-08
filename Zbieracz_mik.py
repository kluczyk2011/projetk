import sounddevice as sd
import numpy as np
import time
import csv

def get_volume():
    audio = sd.rec(int(0.3 * fs), channels=1)  # Record audio for 5 seconds
    sd.wait()  # Wait until recording is finished
    volume = np.abs(audio).mean()  # Calculate the average absolute amplitude
    return volume

# Set the sampling frequency (44100 Hz is a common value)
fs = 44100
pressure = 0

fieldnames = ["pressure", "voltage"]

with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

# Infinite loop to check the volume every 5 seconds
while True:
    voltage = get_volume()
    print(f"voltage: {voltage:.2f}")
    pressure += 1
    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "pressure": pressure,
            "voltage": voltage,
        }

        csv_writer.writerow(info)
        print(pressure, voltage)
    time.sleep(0.6)