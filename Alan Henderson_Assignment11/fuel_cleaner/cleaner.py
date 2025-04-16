# File Name : Alan Henderson_Assignment11
# Student Name: Jack Driehaus, Madison Geier
# email:  driehajl@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date:   04/17/2025
# Course #/Section:   IS4010-002
# Semester/Year:   spring 2025
# Brief Description of the assignment:  clean up some data in a csv file and write the cleaned data into a new file

# Brief Description of what this module does: Cleans up the csv file by doing things like getting rid of the pepsi rows
# Citations: chatgpt.com https://www.zippopotam.us/

# Anything else that's relevant: We could not figure out how to use the zipcodebase API you provided so we used zippopotam.us which is basically the same thing and it worked


import re

class FuelDataCleaner:
    def __init__(self, api_client):
        self.api_client = api_client
        self.zip_cache = {}  # cache to avoid repeated API calls for the same city/state

    def has_zip(self, full_address):
        return bool(re.search(r'\b\d{5}\b$', full_address.strip()))

    def extract_city_state(self, full_address):
        try:
            parts = [part.strip() for part in full_address.split(',')]
            city = parts[1]
            state = parts[2].split()[0]
            return city.title(), state.upper()
        except Exception:
            return None, None

    def clean_data(self, rows):
        unique_rows = []
        seen = set()
        anomalies = []

        for row in rows:
            row_tuple = tuple(sorted(row.items()))
            if row_tuple in seen:
                continue
            seen.add(row_tuple)

            if 'pepsi' in row.get('Fuel Type', '').lower():
                anomalies.append(row)
                continue

            try:
                row['Gross Price'] = f"{float(row['Gross Price']):.2f}"
            except:
                row['Gross Price'] = "0.00"

            full_address = row.get('Full Address', '')
            if full_address and not self.has_zip(full_address):
                city, state = self.extract_city_state(full_address)
                if city and state:
                    cache_key = (city, state)
                    if cache_key in self.zip_cache:
                        zip_code = self.zip_cache[cache_key]
                    else:
                        zip_code = self.api_client.get_zip_code(city, state)
                        self.zip_cache[cache_key] = zip_code

                    if zip_code:
                        row['Full Address'] = full_address.strip().rstrip(',') + f' {zip_code}'

            unique_rows.append(row)

        return unique_rows, anomalies

