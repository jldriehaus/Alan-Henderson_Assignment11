# File Name : Alan Henderson_Assignment11
# Student Name: Jack Driehaus
# email:  driehajl@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date:   04/17/2025
# Course #/Section:   IS4010-002
# Semester/Year:   spring 2025
# Brief Description of the assignment:  clean up some data in a csv file and write the cleaned data into a new file

# Brief Description of what this module does: Cleans up the csv file by doing things like getting rid of the pepsi rows
# Citations: chatgpt.com

# Anything else that's relevant:


class FuelDataCleaner:
    def __init__(self, api_client):
        self.api_client = api_client

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

            if row.get('City') and row.get('Full Address') and not any(char.isdigit() for char in row['Full Address'][-5:]):
                zip_code = self.api_client.get_zip_code(row['City'])
                if zip_code:
                    row['Full Address'] += f' {zip_code}'


            unique_rows.append(row)

        return unique_rows, anomalies

