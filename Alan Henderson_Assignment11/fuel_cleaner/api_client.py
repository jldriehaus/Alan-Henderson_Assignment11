# File Name : Alan Henderson_Assignment11
# Student Name: Jack Driehaus, Madison Geier
# email:  driehajl@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date:   04/17/2025
# Course #/Section:   IS4010-002
# Semester/Year:   spring 2025
# Brief Description of the assignment:  clean up some data in a csv file and write the cleaned data into a new file

# Brief Description of what this module does: Gets the zip code for the addresses that are missing one
# Citations: chatgpt.com https://www.zippopotam.us/

# Anything else that's relevant: We could not figure out how to use the zipcodebase API you provided so we used zippopotam.us which is basically the same thing and it worked


import requests

class ZipCodeAPIClient:
    def get_zip_code(self, city, state):
        try:
            city_url = city.lower().replace(" ", "%20")
            url = f"https://api.zippopotam.us/us/{state}/{city_url}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return data['places'][0]['post code']
        except Exception:
            pass
        return None

