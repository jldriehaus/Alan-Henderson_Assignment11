

# File Name : Alan Henderson_Assignment11
# Student Name: Jack Driehaus, Madison Geier
# email:  driehajl@mail.uc.edu, geierml@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date:   04/17/2025
# Course #/Section:   IS4010-002
# Semester/Year:   spring 2025
# Brief Description of the assignment:  clean up some data in a csv file and write the cleaned data into a new file

# Brief Description of what this module does: Instantiates the functions from the other modules and prints what it is doing
# Citations: chatgpt.com https://www.zippopotam.us/ 

# Anything else that's relevant: We could not figure out how to use the zipcodebase API you provided so we used zippopotam.us which is basically the same thing and it worked

# main.py

import os
from fuel_cleaner.file_manager import FileManager
from fuel_cleaner.api_client import ZipCodeAPIClient
from fuel_cleaner.cleaner import FuelDataCleaner

if __name__ == '__main__':
    DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Data'))
    INPUT_FILE = os.path.join(DATA_DIR, 'fuelPurchaseData.csv')
    CLEANED_FILE = os.path.join(DATA_DIR, 'cleanedData.csv')
    ANOMALY_FILE = os.path.join(DATA_DIR, 'dataAnomalies.csv')

    os.makedirs(DATA_DIR, exist_ok=True)

    file_manager = FileManager(INPUT_FILE, ANOMALY_FILE, CLEANED_FILE)
    api_client = ZipCodeAPIClient() 
    cleaner = FuelDataCleaner(api_client)

    print("Reading data...")
    rows = file_manager.read_csv()

    print("Cleaning data...")
    cleaned, anomalies = cleaner.clean_data(rows)

    fieldnames = rows[0].keys() if rows else []

    print("Writing cleaned data...")
    file_manager.write_csv(CLEANED_FILE, fieldnames, cleaned)

    print("Writing anomalies...")
    file_manager.write_csv(ANOMALY_FILE, fieldnames, anomalies)

    print(f"Cleaned data written to: {CLEANED_FILE}")
    print(f"Anomalies written to: {ANOMALY_FILE}")