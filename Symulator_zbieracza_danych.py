import csv
import random as rnd
import time

def log_data():
    pressure = 0
    voltage = 0
    fieldnames = ["pressure", "voltage"]

    with open('data.csv', 'w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()

      # Flag variable to control the loop

    while running:
        with open('data.csv', 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            info = {
                "pressure": pressure,
                "voltage": voltage,
            }

            csv_writer.writerow(info)
            print(pressure, voltage)

            pressure += 1
            voltage = rnd.randint(1, 8)

        time.sleep(1)

        # Check if termination is requested
        # You can set the "running" variable to False from another part of the code
        # to terminate the loop.
        # For example, you can have a button in your GUI that sets "running" to False.
        if not running:
            break
