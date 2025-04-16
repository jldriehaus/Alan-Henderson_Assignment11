# File Name : Alan Henderson_Assignment11
# Student Name: Jack Driehaus
# email:  driehajl@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date:   04/17/2025
# Course #/Section:   IS4010-002
# Semester/Year:   spring 2025
# Brief Description of the assignment:  clean up some data in a csv file and write the cleaned data into a new file

# Brief Description of what this module does: Gets the zip code for the addresses that are missing one
# Citations: chatgpt.com

# Anything else that's relevant:


import requests

class ZipCodeAPIClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://app.zipcodebase.com/api/v1/search"

    def get_zip_code(self, city):
        try:
            response = requests.get(self.base_url, params={
                'apikey': self.api_key,
                'city': city,
                'country': 'US'
            })
            response.raise_for_status()
            data = response.json()
            if data.get('results'):
                return data['results'][0]['postal_code']
        except Exception as e:
            print(f"Failed to retrieve ZIP for {city}: {e}")
        return None

