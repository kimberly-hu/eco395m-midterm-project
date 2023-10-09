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


rates_columns = ['Algebra_Rate', 'Biology_Rate', 'English_Rate', 'US_History_Rate']
print(education_data[rates_columns].describe())

# Clean education data - remove observations with negative values in rates (i.e. missing data)
education_data[rates_columns] = education_data[rates_columns].map(lambda x: x if x >= 0 else np.nan)
education_clean = education_data.dropna(subset = rates_columns)




