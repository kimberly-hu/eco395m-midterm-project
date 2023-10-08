import os
import csv
import requests
import json
import time
from operator import itemgetter

from bs4 import BeautifulSoup


def request_counties_raw_data():
    """
    Send a request for the data from the SRCC website. Use the "request.get" function to extract the dictionary of different counties.
    
    Return:
    raw counties data response object
    """

    counties_url = "https://www.srcc.tamu.edu/climate_data_portal/getCountyClimdivColorInState/?state=TX&countyclimdiv=-1&searchmethod=county&output=json"

    response = requests.get(url=counties_url)
    counties_data = response.json()

    return counties_data

def extract_list_of_counties(counties_data):
    """
    Generate a dictionary for each county that contains "geoid" and "county_name"
    Return as a list

    Return:
    List of dictionaries where each dictionary contains "geoid", "county_name" as keys and their values

    list_of_counties = [{
          "geoid": "48001",
          "county_name": "Anderson County"
        },...]
    """
    counties = counties_data["nocolorgeojson"]["features"]

    list_of_counties = []
    for county in counties:
        d = {}
        d["geoid"] = county["properties"]["geoid"]
        d["county_name"] = county["properties"]["name"]
        list_of_counties.append(d)

    return list_of_counties



def extract_list_of_stations(list_of_counties):
    """
    For each county, add list of stations, call request_stations_raw_data() for each geoid

    list_of_counties = [{
          "geoid": "48001",
          "county_name": "Anderson County"
        },...]
    
    Return:
    list of dictionaries of counties and their stations
    [{
        "geoid": -,
        "county_name": -,
        "stations": [...]
    }]
    """
    num_counties = str(len(list_of_counties))
    print("Getting list of stations for " + num_counties + " counties")

    i = 0
    for county in list_of_counties:
        time.sleep(1)
        geoid = county["geoid"]
        county["stations"] = request_stations_raw_data(geoid)
        print("Got stations for " + county["county_name"] + ", " + str(i+1) + "/" + num_counties)
        i += 1

    return list_of_counties


def request_stations_raw_data(geoid):
    """
    Send "requests.get" to extract dictionary of station ids from SRCC website.

    Response data:
    {{"type": "FeatureCollection", "features": [{"type": "Feature", "geometry": {"type": "Point", "coordinates": [-95.70639, 31.77972]}, "properties": {"title": "PALESTINE MUNICIPAL AP", "sid": "93983", "sid-type": "1", ...}}

    stations_ids = [{"title": "PALESTINE MUNICIPAL AP", "sid": "93983"},{},...]
    """
    station_ids = []

    station_url = "https://www.srcc.tamu.edu/climate_data_portal/getStnsInCountyClimdiv/?countyclimdiv=" + geoid + "&searchmethod=county&typedata=annualsum&year=2018&month=0&element=maxt&output=json"

    response = requests.get(url=station_url)
    station_dict = response.json()

    stations = station_dict["features"]
    for s in stations:
        d = {}
        d["station_name"] = s["properties"]["title"]
        d["station_id"] = s["properties"]["sid"]
        station_ids.append(d)

    return station_ids


def extract_min_max(list_of_counties):
    """
    For each county, iterate through stations until one successful min and max temp extraction
    
    list_of_counties:
    [{
        "geoid": -,
        "county_name": -,
        "stations": [{"title": "PALESTINE MUNICIPAL AP", "sid": "93983"},{},...]
    },...]

    Use "BeautifulSoup" to extract the monthly minimum and maximum temperature tables to create a list using sid

    Return:
    [{
        "geoid": -,
        "county_name": -,
        "stations": [{"title": "PALESTINE MUNICIPAL AP", "station_id": "93983"},{},...],
        "station_id_2018": -,
        "station_id_2019": -,
        "min_temps_2018": [...],
        "max_temps_2018": [...],
        "min_temps_2019": [...],
        "max_temps_2019": [...]
    }]
    """

    num_counties = str(len(list_of_counties))
    print("Processing " + num_counties + " counties")

    i = 0
    for county in list_of_counties:
        time.sleep(2)
        for year in ["2018", "2019"]:
            max_temp_key = "max_temps_" + year
            min_temp_key = "min_temps_" + year
            station_key = "station_id_" + year

            for station in county["stations"]:
                temps_dict = request_temps_raw_data(station["station_id"], year)
                temps_table = temps_dict["table"]

                soup = BeautifulSoup(temps_table, "html.parser")
                data_tables = soup.findAll("table")
                table = data_tables[-1]

                if not table:
                    continue

                max_row = table.find("th", string="Max").find_parent("tr")
                min_row = table.find("th", string="Min").find_parent("tr")

                max_values = [td.get_text() for td in max_row.find_all("td")]
                min_values = [td.get_text() for td in min_row.find_all("td")]

                bad_value = False
                for max_val in max_values:
                    if max_val == "M":
                        bad_value = True
                for min_val in min_values:
                    if min_val == "M":
                        bad_value = True
                if bad_value:
                    continue

                county[max_temp_key] = [int(k) for k in max_values]
                county[min_temp_key] = [int(k) for k in min_values]
                county[station_key] = station["station_id"]

                break

            # only need to check either max_temp or min_temp since both get added only if both have all valid values
            if max_temp_key not in county:
                county[max_temp_key] = []
                county[min_temp_key] = []
                county[station_key] = ""
                print("Valid temps not found for county " + county["county_name"] + " in year " + year)
        print("Finished county " + county["county_name"] + ", " + str(i+1) + "/" + num_counties)
        i += 1
            
    return list_of_counties


def request_temps_raw_data(sid, year):
    """
    Use "requests.get" to extract monthly min and max temps for the each station. 

    Return:
    Dictionary that gets returned has the temps in a key "table"
    """
    
    temps_url = "https://www.srcc.tamu.edu/climate_data_portal/getDataInStn/?sid=" + sid + "&year=" + year + "&elem=maxt&output=json"

    response = requests.get(url=temps_url)
    temps_data = response.json()

    return temps_data


def average_min_max(temps_data):
    """
    Take the monthly min and max and calculate the average from 08-01-2018 to 06-01-2019. Add as values to dictionary

    temps_data:
    [{
        "geoid": -,
        "county_name": -,
        "stations": [{"title": "PALESTINE MUNICIPAL AP", "station_id": "93983"},{},...],
        "station_id_2018": -,
        "station_id_2019": -,
        "min_temps_2018": [...],
        "max_temps_2018": [...],
        "min_temps_2019": [...],
        "max_temps_2019": [...]
    },...]

    
    Return:
    [{
        "geoid": -,
        "county_names": -,
        "stations": [{"title": "PALESTINE MUNICIPAL AP", "station_id": "93983"},{},...],
        "station_id_2018": -,
        "station_id_2019": -,
        "min_temps_2018": [...],
        "max_temps_2018": [...],
        "min_temps_2019": [...],
        "max_temps_2019": [...]
        "avg_min_temp": -,
        "avg_max_temp": -
    },...]
    """

    for county in temps_data:
        max_temps = county["max_temps_2018"][7:]+county["max_temps_2019"][:6]
        min_temps = county["min_temps_2018"][7:]+county["min_temps_2019"][:6]
        county["avg_max_temp"] = round(sum(max_temps)/len(max_temps),2) if max_temps else ""
        county["avg_min_temp"] = round(sum(min_temps)/len(min_temps),2) if min_temps else ""
   

    return temps_data


def sort_data(final_temp_data):
    """
    Sort data by county name

    Return:
    sorted data
    """
    sorted_data = sorted(final_temp_data, key=itemgetter("county_name"))

    return sorted_data


def write_to_csv(sorted_data, path):
    """
    Write the data to a csv with order:
    "county_name", "geoid", "station_id_2018","station_id_2019", "avg_max_temp", "avg_min_temp"
    """
    
    with open(path, "w", newline="") as csvfile:
        fieldnames = ["county_name", "geoid", "station_id_2018","station_id_2019", "avg_max_temp", "avg_min_temp"]
        writer = csv.writer(csvfile)
        writer.writerow(fieldnames)
        for county in sorted_data:
            writer.writerow([county["county_name"], county["geoid"], county["station_id_2018"], county["station_id_2019"], county["avg_max_temp"], county["avg_min_temp"]])

    return


if __name__ == "__main__":

    base_dir = "data/temp_data/"
    csv_path = os.path.join(base_dir, "temp_data.csv")

    os.makedirs(base_dir, exist_ok=True)

    counties_data = request_counties_raw_data()
    list_of_counties = extract_list_of_counties(counties_data)
    counties_with_stations = extract_list_of_stations(list_of_counties)
    
    # save list of counties with stations to file
    stations_path = "data/temp_data/counties_with_stations.json"
    with open(stations_path, "w") as stations_file:
        json.dump(counties_with_stations, stations_file)
    
    counties_with_stations = []
    with open(stations_path, encoding="utf-8") as f:
        counties_with_stations = json.loads(f.read())

    counties_with_stations_temps = extract_min_max(counties_with_stations)
    
    # save list of counties with temps to file
    counties_with_stations_temps_path = "data/temp_data/temps.json"
    with open(counties_with_stations_temps_path, "w") as temps_file:
        json.dump(counties_with_stations_temps, temps_file)

    counties_with_stations_temps = []
    with open(counties_with_stations_temps_path, encoding="utf-8") as f:
        counties_with_stations_temps = json.loads(f.read())

    # calculate averages, sort, and write to csv
    final_temp_data = average_min_max(counties_with_stations_temps)
    sorted_data = sort_data(final_temp_data)
    write_to_csv(sorted_data, csv_path)
