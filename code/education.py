import numpy as np
import pandas as pd
import os

FILEPATH = "data/education_data/"
OUTPATH = os.path.join(FILEPATH, "education_data.csv")

academic_data = pd.read_csv(os.path.join(FILEPATH, "academic_data.csv"))
staff_data = pd.read_csv(os.path.join(FILEPATH, "staff_data.csv"))
campus_reference_data = pd.read_csv(os.path.join(FILEPATH, "campus_reference_data.csv"))
regions_info = pd.read_csv(os.path.join(FILEPATH, "regions_info.csv"))


# attach region names to campus reference

def format_region(value):
    """Transform the data type of REGION from integer to string."""

    return f"'{value:02d}"


regions_info["REGION_str"] = pd.Series(regions_info["REGION"]).apply(format_region)

campus_reference_data_1 = campus_reference_data.merge(
    regions_info[["REGION_str", "CITY"]],
    how="left",
    left_on="REGION",
    right_on="REGION_str",
)

campus_reference_data_1 = campus_reference_data_1.drop(columns=["REGION_str"])


campus_colnames = {
    "CAMPUS": "Campus",
    "CAMPNAME": "Campus_Name",
    "CNTYNAME": "County_Name",
    "COUNTY": "County",
    "DISTNAME": "District_Name",
    "DISTRICT": "District",
    "REGION": "Region",
    "CITY": "Region_Name",
}
campus_reference_data_1.rename(columns=campus_colnames, inplace=True)


# keep relevant columns in academic data

academic_data_1 = academic_data[
    ["CAMPUS", "CDA00AA11219R", "CDA00ABI1219R", "CDA00AR11219R", "CDA00AUS1219R"]
]

academic_colnames = {
    "CAMPUS": "Campus",
    "CDA00AA11219R": "Algebra_Rate",
    "CDA00ABI1219R": "Biology_Rate",
    "CDA00AR11219R": "English_Rate",
    "CDA00AUS1219R": "US_History_Rate",
}
academic_data_1.rename(columns=academic_colnames, inplace=True)


# remove observations missing student performance data

academic_data_2 = academic_data_1.replace(".", np.nan)
subject_columns = ["Algebra_Rate", "Biology_Rate", "English_Rate", "US_History_Rate"]
academic_data_2 = academic_data_2.dropna(subset=subject_columns)


# keep relevant columns in staff data

staff_col_drop = [
    "CPCTG01A",
    "CPCTG02A",
    "CPCTG03A",
    "CPCTG04A",
    "CPCTG05A",
    "CPCTG06A",
    "CPCTGKGA",
    "CPCTGMEA",
    "CPCTFLAA",
]
staff_data_1 = staff_data.drop(columns=staff_col_drop)

staff_colnames = {
    "CAMPUS": "Campus",
    "CPCTENGA": "Class_Size_English",
    "CPCTMATA": "Class_Size_Math",
    "CPCTSCIA": "Class_Size_Sci",
    "CPCTSOCA": "Class_Size_Soc_Stud",
    "CPST00FC": "Teacher_Beginning_Count",
    "CPST00FP": "Teacher_Beginning_Percent",
    "CPST01FC": "Teacher_1-5_Years_Count",
    "CPST01FP": "Teacher_1-5_Years_Percent",
    "CPST06FC": "Teacher_6-10_Years_Count",
    "CPST06FP": "Teacher_6-10_Years_Percent",
    "CPST11FC": "Teacher_11-20_Years_Count",
    "CPST11FP": "Teacher_11-20_Years_Percent",
    "CPST20FC": "Teacher_More_Than_20_Years_Count",
    "CPST20FP": "Teacher_More_Than_20_Years_Percent",
    "CPSTBAFC": "Teacher_BA_Degree_Count",
    "CPSTBAFP": "Teacher_BA_Degree_Percent",
    "CPSTEXPA": "Teacher_Experience_Average",
    "CPSTKIDR": "Teacher_Student_Ratio",
    "CPSTMSFC": "Teacher_MS_Degree_Count",
    "CPSTMSFP": "Teacher_MS_Degree_Percent",
    "CPSTNOFC": "Teacher_No_Degree_Count",
    "CPSTNOFP": "Teacher_No_Degree_Percent",
    "CPSTPHFC": "Teacher_PH_Degree_Count",
    "CPSTPHFP": "Teacher_PH_Degree_Percent",
    "CPSTTENA": "Teacher_Tenure_Average",
}
staff_data_1.rename(columns=staff_colnames, inplace=True)

print(staff_data_1.head(5))


# merge academic data, staff data and campus reference

education_data = academic_data_2.merge(staff_data_1, how="left", on="Campus")

education_data = education_data.merge(campus_reference_data_1, how="left", on="Campus")

print(education_data.head(5))

education_data.to_csv(OUTPATH)
