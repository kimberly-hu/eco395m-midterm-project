import numpy as np
import pandas as pd

education_data = pd.read_csv("data/education_data/education_data.csv", index_col=0)
census_data = pd.read_csv("data/census_data/census_data.csv")
temp_data = pd.read_csv("data/temp_data/temp_data.csv")


print(education_data.head(5))

# Clean education data - put strings in nice formats
education_data['Campus'] = education_data['Campus'].str[1:]
education_data['County'] = education_data['County'].str[1:]
education_data['District'] = education_data['District'].str[1:]
education_data['Region'] = education_data['Region'].str[1:]
education_data['Region_Name'] = education_data['Region_Name'].str.upper()


print(education_data.dtypes)

# Clean education data - convert some integers/strings to floats
education_data = education_data.replace('.', np.nan)

for col in education_data.columns[1:5]:
    education_data[col] = education_data[col].astype(float)

for col in education_data.columns[5:30]:
    education_data[col] = pd.to_numeric(education_data[col])


# We observed negative values (-1) in student performance. Theses are missing data and should be removed.
rates_columns = ['Algebra_Rate', 'Biology_Rate', 'English_Rate', 'US_History_Rate']
print(education_data[rates_columns].describe())

education_data[rates_columns] = education_data[rates_columns].map(lambda x: x if x >= 0 else np.nan)
education_clean = education_data.dropna(subset = rates_columns)


print(census_data.head(5))

census_colnames = {
    'B19013_001E': 'Median_Household_Income', 
    'B19083_001E': 'Gini_Index', 
    'B19113_001E': 'Median_Family_Income',
                  }

census_data.rename(columns = census_colnames, inplace = True)

print(census_data.dtypes)

# County codes in education data and census data do not match, so we need to merge on county names.
# Convert county name in census data into the same format as in education data. 
census_data['County_Name'] = census_data['NAME'].str.upper()
census_data['County_Name'] = census_data['County_Name'].str[:-14]


# Merge census data to education data on county name.
merged_data = education_clean.merge(census_data[['County_Name', 'Median_Household_Income', 'Gini_Index', 'Median_Family_Income', 'Poverty_Rate']], 
                                   how = 'left', 
                                   left_on = 'County_Name',
                                   right_on = 'County_Name'
                                  )
print(merged_data.head(5))


print(temp_data.head(5))

temp_data.rename(columns={'avg_max_temp':'Avg_Max_Temp', 
                          'avg_min_temp':'Avg_Min_Temp'
                          }, 
                          inplace=True)

print(temp_data.dtypes)

# Convert county codes in temperature data to the same format as in education data.
temp_data['geoid'] = temp_data['geoid'].astype(str)
temp_data['County'] = temp_data['geoid'].str[2:]

print(temp_data.head(5))


# Merge temperature data on county code
all_data = merged_data.merge(temp_data[['Avg_Max_Temp', 'Avg_Min_Temp', 'County']],
                             how='left',
                             on='County')

print(all_data.head(5))

all_data.to_csv('data/all_data.csv', index=False)
