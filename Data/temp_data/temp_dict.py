
"""
Game plan
    Use the "request raw data" to make a request for all counties in Texas that returns a list of counties
    Using that data create a dictionary of all the counties in Texas that have the GEOID and county name as keys in the dictionaries of each county
    After the variable "GEOID" is established, use that variable for the "request raw data" url for station level data
    Use that data to create a list of stations with "stationid (sid)" and "station name (title)" as the keys in each station dictionary
    After the sid is obtained, use that to plug into the url for "request raw data" for the actual monthly min and max temperatures.
    Use the "BeautifulSoup" library to extract the monthly min and max values from given code
    Then create a dictionary for each stationid that contains "min" and "max" as keys in the dictionary
"""

import os
import csv

import requests



def request_counties_raw_data():
    # Send a request for the data from the SRCC website. Use the "request.get" function to extract the dictionary of different counties.

    counties_url = "https://www.srcc.tamu.edu/climate_data_portal/getCountyClimdivColorInState/?state=TX&countyclimdiv=-1&searchmethod=county&output=json"

    response = requests.get(url=counties_url)
    counties_data = response.json()

    return counties_data

def extract_list_of_counties(counties_data):
    """
    Generate a dictionary for each county that contains "GEOID" and "name"
    Return as a list
    """

    list_of_counties = []
    # for count in counties_data:
    #     d = {}
    #     # d["geoid"] = count[]


    return list_of_counties



def extract_list_of_stations(list_of_counties):
    """
    For each county, add list of stations, call request_stations_raw_data() for each geoid
    list_of_counties = [{
          "geoid": "48001",
          "name": "Anderson County"
        },...]
    
    Return list of dictionary of stations
    [{
        "geoid": -,
        "name": -,
        "stations": [...]
    }]
    """
    list_of_stations = []

    return list_of_stations


def request_stations_raw_data(geoid):
    """
    Send "requests.get" to extract dictionary of station ids from SRCC website.

    Response data:
    {{"type": "FeatureCollection", "features": [{"type": "Feature", "geometry": {"type": "Point", "coordinates": [-95.70639, 31.77972]}, "properties": {"title": "PALESTINE MUNICIPAL AP", "sid": "93983", "sid-type": "1", ...}}

    stations_ids = [{"title": "PALESTINE MUNICIPAL AP", "sid": "93983"},{},...]

    MAKE SURE TO ADD AN OPTION FOR EMPTY LIST IF NO STATIONS EXIST
    """
    station_ids = []


    return station_ids


def extract_min_max(list_of_stations):
    """

    For each county, iterate through stations until one successful min and max temp extraction
    

    list_of_stations:
    [{
        "geoid": -,
        "name": -,
        "stations": [{"title": "PALESTINE MUNICIPAL AP", "sid": "93983"},{},...]
    }]

    Use "BeautifulSoup" to extract the monthly minimum and maximum temperature tables to create a list using sid

    """
    list_of_min_max = []

    return list_of_min_max

def request_temps_raw_data(sid):
    """
    Use "requests.get" to extract monthly min and max temps for the each station. 
    """
    temps_data = []

    return temps_data


def average_min_max(temps_data):
    """
    Take the monthly min and max and calculate the average from 08-01-2018 to 06-01-2019. Add as values to dictionary

    temps_data:
    [{
        "geoid": -,
        "name": -,
        "stations": [{"title": "PALESTINE MUNICIPAL AP", "sid": "93983"},{},...],
        "sid": -,
        "min_temps": [...],
        "max_temps": [...]
    }]


    """
    final_temps_data= []

    return final_temps_data

def sort_data(final_temps_data):
    """
    Sort data by county name
    """

    return sorted_data

def write_to_csv(sorted_data):
    """Write the data to a csv with the list:
        "county_name"
        "GEOID"
        "station id"
        "station_title"
        "avg_max"
        "avg_min"
        """
    
    return 

if __name__ == "__main__":

    BASE_DIR = "temp_data"
    CSV_PATH = os.path.join(BASE_DIR, "temp_data.csv")

    os.makedirs(BASE_DIR, exist_ok=True)

    counties_data = request_counties_raw_data()
    print(counties_data)
    # list_of_counties = extract_list_of_counties(counties_data)
    # list_of_stations = extract_list_of_stations(list_of_counties)
    # list_of_temps = extract_min_max(list_of_stations)
    # final_temp_data = average_min_max(list_of_temps)
    # sorted_data = sort_data(final_temp_data)
    # write_to_csv(sorted_data, CSV_PATH)
