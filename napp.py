import csv

file_path = r"C:\Users\Doge\Desktop\projekt od wjerzana\Nap.TRA"

def read_csv_file(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file, delimiter=';')
            columns = []
            for row in reader:
                columns.append(row)
            print(columns[8])

    except FileNotFoundError:
        print("File not found.")

# Example usage
read_csv_file(file_path)
