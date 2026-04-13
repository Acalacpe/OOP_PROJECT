from FileReaderWriter import FileReaderWriter
import csv
import os

class CSVFileReaderWriter(FileReaderWriter):
    def read(self, filepath, column_name=None):
        data = []
        try:
            with open(filepath, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                if column_name:
                    for row in reader:
                        if row.get(column_name):
                            data.append(row[column_name].lower())
                else:
                    for row in reader:
                        data.append(row)
            return sorted(data, key=len, reverse=True)
        except FileNotFoundError:
            print(f"Warning: {filepath} not found")
            return []
        except Exception as e:
            print(f"Error reading {filepath}: {e}")
            return []

    def write(self, filepath, data):
        with open(filepath, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(data)
        