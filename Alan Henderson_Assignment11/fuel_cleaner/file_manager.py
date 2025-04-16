

# File Name : Alan Henderson_Assignment11
# Student Name: Jack Driehaus, Madison Geier
# email:  driehajl@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date:   04/17/2025
# Course #/Section:   IS4010-002
# Semester/Year:   spring 2025
# Brief Description of the assignment:  clean up some data in a csv file and write the cleaned data into a new file

# Brief Description of what this module does: reads and writes the csv files
# Citations: chatgpt.com https://www.zippopotam.us/

# Anything else that's relevant:


import csv

class FileManager:
    def __init__(self, input_path, anomaly_path, cleaned_path):
        self.input_path = input_path
        self.anomaly_path = anomaly_path
        self.cleaned_path = cleaned_path

    def read_csv(self):
        with open(self.input_path, mode='r', encoding='utf-8-sig') as f:
            return list(csv.DictReader(f))

    def write_csv(self, path, fieldnames, rows):
        with open(path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

