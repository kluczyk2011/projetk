import os
import csv
import pandas as pd
import matplotlib.pyplot as plt

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