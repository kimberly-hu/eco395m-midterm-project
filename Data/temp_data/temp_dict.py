
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


    return counties_data

def extract_list_of_counties(counties_data):
    """
    Generate a dictionary for each county that contains "GEOID" and "name"
    Return as a list
    """
    list_of_counties = []

    return list_of_counties



def extract_list_of_stations(list_of_counties):
    """
    For each county, add list of stations, call request_stations_raw_data() for each geoid
    list_of_countiess = [{
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
    {"type": "FeatureCollection", "features": [{"type": "Feature", "geometry": {"type": "Point", "coordinates": [-95.70639, 31.77972]}, "properties": {"title": "PALESTINE MUNICIPAL AP", "sid": "93983", "sid-type": "1", ...}

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
    Take the monthly min and max and calculate the average from 09-01-2018 to 06-01-2019."
    """
    final_temps_data= []

    return final_temps_data

def write_to_csv(final_temps_data):
    """Write the data to a csv with the list:
        "county name"
        "GEOID"
        "station id"
        "station_title"
        "Max"
        "Min"
        """
    return 
