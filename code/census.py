import requests
import pandas as pd

BASE_URL = "https://api.census.gov/data/2019/acs/acs5?get="
VARIABLES = (
    "NAME,B19013_001E,B19083_001E,B19113_001E,B01003_001E,C17002_002E,C17002_003E"
)
GEOGRAPHY = "&for=county:*&in=state:48"
csv_file_path = "data/census_data/census_data.csv"


def request_raw_data():
    """Requests 2019 Texas census data from Census.gov."""

    response = requests.get(url=BASE_URL + VARIABLES + GEOGRAPHY)
    data = response.json()
    return data


def raw_into_df(data):
    """Transforms raw census data into dataframe."""

    df = pd.DataFrame(data[1:], columns=data[0])
    return df


census_data = request_raw_data()
census_df = raw_into_df(census_data)

columns_to_convert = [
    "B19013_001E",
    "B19083_001E",
    "B19113_001E",
    "B01003_001E",
    "C17002_002E",
    "C17002_003E",
]
census_df[columns_to_convert] = census_df[columns_to_convert].astype(float)

# Poverty rate = Population in poverty / Total population
census_df["Poverty_Rate"] = (
    (census_df["C17002_002E"] + census_df["C17002_003E"])
    / census_df["B01003_001E"]
    * 100
)
census_df_final = census_df.drop(["C17002_002E", "C17002_003E", "B01003_001E"], axis=1)

census_df_final.to_csv(csv_file_path, index=False)
