import csv
import random
import time

pressure=0
voltage=0


fieldnames = ["pressure", "voltage"]


with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:

    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "pressure": pressure,
            "voltage": voltage,
        }

        csv_writer.writerow(info)
        print(pressure, voltage)

        pressure += 1
        voltage = random.randint(1, 8)

    time.sleep(1)