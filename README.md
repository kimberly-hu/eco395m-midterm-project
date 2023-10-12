# How to Get the Grade:
# What has the greatest effect on student performance?
October 12, 2022

Alina Khindanova, Audrey Peres, Kimberly Hu, Lydia Liu, & Marco Rodriguez

# Introduction 

Educational achievement in high schools, exemplified by the State of Texas Assessments of Academic Readiness (STAAR) scores, is influenced by many factors, both conventional and unconventional. While determinants like class size, teacher experience, and socioeconomic indicators such as median household income and the GINI index have been frequently explored, this project uniquely integrates environmental factors, specifically average maximum and minimum temperatures. Our study aims to ascertain whether variables like average temperatures, class size, teacher qualifications, and economic indicators can determine the percentage of high school students achieving meeting-level STAAR scores. The ultimate goal is to discern which can serve as robust indicators, enhancing our understanding of the determinants of academic achievement and the potential influences they can have.

# Data

1. Education Data

Education data is retrieved from Texas Education Agency (TEA). All data is from 2018-2019 to avoid the impact of COVID-19 and at campus-level. 

We collected data on campus information, student performance information, class size, and teachers’ information. Campus information includes the details of each campus, such as name and code. Class sizes are the average class size for each type of subject (English, Math, Science, Social Studies). Teachers’ information include teachers’ teaching experience counts and percentages by categories (beginning, 1-5 years, 6-10 years, 11-20 years, > 20 years), teachers’ highest degree counts and percentages by categories (no degree, BA, MS, PhD),  average teaching experience, and average tenure. 

Student academic performance data is based on STAAR: The State of Texas Assessments of Academic Readiness. It is a standardized academic achievement test for all Texas students. Students taking high school courses are assessed through STAAR end-of-course (EOC) exams. We selected “meets grade level” variables as our variables of interest, which measure the percentage of students who reach the "meet" level (shows strong knowledge of course content; student is prepared to progress to the next grade). 

2. Temperature Data

All temperature data is collected from the Southern Regional Climate Center (SRCC). The average monthly temperatures (Fahrenheit) were pulled from August 1, 2018, to June 1, 2019, to account for the temperatures during an average school year. 

The data provided for temperatures are:
County name
- Geo ID (code for each individual county)
- Station ID (code for each individual station)
- Average maximum temperature for the county
- Average minimum temperature for the county

3. Income, Inequality, and Poverty Data

Census related data were collected through the Census Bureau API, specifically drawing from the American Community Survey 5-Year data estimates provided by the U.S. Census Bureau. The initial step involved a review of the API documentation to gain insight into data retrieval processes, complemented by practical examples. Furthermore, a comprehensive list of variables accessible via the API was consulted to determine the pertinent data components. We retrieved data at the county level in Texas, including median household income, median family income, the Gini index, population with the ratio of income to poverty level below 1, and total population. Requests were designed to access the 2019 dataset for these variables.


# Running the Code

Our code will be executed in a Python 3 environment and required packages can be installed with `pip install -r requirements.txt`. The project can be reproduced by running the following scripts in order, at the top of the repo: “census.py”, “temp_dict.py”, “all_data.py”, “analysis.py”. All code files are stored under the “code” folder. 

census.py utilizes the Census Bureau API and pulls data related to income, inequality and poverty through get requests. It also calculates the poverty rate as the population with income below the poverty level divided by total population. 

temp_dict.py utilizes the API from SRCC to extract a list of counties in Texas, look for the list of weather stations for each county, and calculate average temperatures for each county based on stations. Beautifulsoup is used to extract the temperature data from the different stations. 
(not sure what to say here, seems to have duplicates with methodology)

all_data.py first calls on education.py to merge datasets related to education based on campus, then merges the education data with census data and temperature data based on county. The datasets are cleaned and manipulated using pandas. Observations missing student performance data are removed from our dataset for analysis. 

analysis.py reads the merged dataset and produces our results, including summary statistics of all variables, scatter plots between student performance and each variable, correlation tables on selected independent variables, and linear regression results. All results are stored in the “artifacts” folder. 


# Methodology

1. Data Collection and Merge

1.1 Education Data

Education data can be downloaded from this link. We selected “campus download” under “all records”, and downloaded the following datasets: “Campus Reference”, “Staff information”, “STAAR Approaches Grade Level, Meets Grade Level, and Masters Grade Level (All Grades) 2019”. Additionally, we obtained “ESC Regions Information” from TEA Public Open Data Site. 

Campus reference data was downloaded with the following options:
- Campus Name
- County Name & Number
- District Name & Number
- Region Name & Number

Class size and teachers data was downloaded with the following options: 
- Class Size Averages
- Teachers by Highest Degree
- Teachers by Year of Experience
- Teachers: Experience Average, Tenure Average, Student Ratio

Student performance data was downloaded with the following options: 
- EOC English I, Meets Grade Level, 2019
- EOC Algebra I, Meets Grade Level, 2019
- EOC Biology, Meets Grade Level, 2019
- EOC US History, Meets Grade Level, 2019

All datasets were saved as CSV files in the “education_data” folder under “data”: 
- “Campus Reference”: campus_reference_data.csv
- “Staff information”: staff_data.csv
- “STAAR Approaches Grade Level, Meets Grade Level, and Masters Grade Level (All Grades) 2019”: academic_data.csv
- “ESC Regions Information”: regions_info.csv

1.2 Temperature Data

Data was extracted using an API to pull the monthly average temperatures for individual stations, the county that the stations are located in, and the codes for the stations (stationid) and counties (geoid). 

Once the data was pulled from the SRCC website, the average maximum and minimum temperatures were calculated by collecting all monthly averages for each station within each county and averaging those into one temperature reading for the allotted time period. Once the station level averages were calculated, one of the stations within a county was chosen as the representative station. 

1.3 Census Data

Data was extracted using the Census Bureau API to pull income, inequality and variables needed to calculate poverty level through get requests. We also calculated the poverty rate. All these variables. All these variables correspond to 2019 at a county level. 

2. Exploratory Analysis

We employ Python to analyze the relationship between each variable and student academic performance across various courses, and export scatter graphs stored at scatter_plots under artifacts. The findings indicate that the following 8 exploratory variables significantly influence the dependent variable, which is student academic performance.

Exploratory Variables: 
- "Avg_Max_Temp",
- "Avg_Min_Temp",
- "Class Size by Subject (e.g. Class_Size_English)",
- "Teacher_Experience_Average",
- "Teacher_MS_Degree_Percent",
- "Median_Household_Income",
- "Gini_Index",
- "Poverty_Rate"

Dependent Variables: 
- "Student Academic Performance by Subject, (e.g. English_Rate)"

3. Correlation and Linear Regression

We use Python to run matrix graphs that display correlations among 9 variables (See graphs in Results). The objective of presenting these correlations is to identify any relationships between any two variables that might introduce bias into the regression results.

To investigate the influence of class size and average teaching experience on student academic performance in subjects such as English, Biology, US History and Math, we conducted Ordinary Least Squares (OLS) regression analysis. These academic performance scores served as the dependent variables in our study. The key variables of interest were class size and average teaching experience. Additionally we also included other previously mentioned explanatory variables as control variables. It’s worth noting that we excluded data points with missing values in the OLS estimation.

# Results

We did not find any of the variables used as control variables, including average maximum temperature, average minimum temperature, median household income, GINI index, or poverty rate to be significant at a level of 1% or less. Therefore, they were used as control variables in our regression.

The results of the Ordinary Least Squares (OLS) estimation reveal significant effects for both class size and the average teacher experience on student academic performance in all four subjects (with a P-value less than 0.01). Also, the impact of class size is more clear cut in the field of biology. Specifically, adding one additional student to the class leads to a 0.1928 increase in the algebra rate, a substantial 1.3372 increase in biology, a notable 1.0083  increase in English, and a solid 0.9804 increase in US history.

Furthermore, the effect of teaching experience is most prominent in biology, although it also exhibits a notable influence on English. The analysis indicates that a one-year increase in the average teaching experience results in a 0.6153 percentage point rise in the algebra rate, a 0.6654 increase in biology, a 0.6657 increase in English and a 0.4978 increase in US history.

We also observed a significant impact of the percentage of teachers with master’s degrees on academic performance in all subjects. The most substantial effect was seen in English, a 1 percentage point increase in the percentage of teachers with master’s degrees resulted in a significant 0.2471 increase in academic performance rate. 

![correlation_matrix_english](https://github.com/kimberly-hu/eco395m-midterm-project/assets/143051809/303592e6-c1e7-4d25-9e5a-1113f1db1be7)

<img width="652" alt="Screenshot 2023-10-12 at 7 08 08 AM" src="https://github.com/kimberly-hu/eco395m-midterm-project/assets/143051809/1d5334a6-7448-489c-ae17-0984d8848723">

![correlation_matrix_math](https://github.com/kimberly-hu/eco395m-midterm-project/assets/143051809/039ab85a-4eda-4665-875c-5825cbf14c9e)

<img width="652" alt="Screenshot 2023-10-12 at 7 10 18 AM" src="https://github.com/kimberly-hu/eco395m-midterm-project/assets/143051809/43c1e51a-7136-4fd6-855c-1e46fa58dae5">

![correlation_matrix_sci](https://github.com/kimberly-hu/eco395m-midterm-project/assets/143051809/c92b337a-daca-4602-a864-bea3acef14f0)

<img width="652" alt="Screenshot 2023-10-12 at 7 12 42 AM" src="https://github.com/kimberly-hu/eco395m-midterm-project/assets/143051809/b4f5547a-7306-4427-a7ea-2503dede6d59">

![correlation_matrix_soc_stud](https://github.com/kimberly-hu/eco395m-midterm-project/assets/143051809/87ff9a28-7d3e-4a4c-8cd4-a5f5cfafa8b0)

<img width="652" alt="Screenshot 2023-10-12 at 7 14 08 AM" src="https://github.com/kimberly-hu/eco395m-midterm-project/assets/143051809/8155aab3-b778-44aa-b4bd-a32e8f855f27">


# Limitations and Extensions
Data:

The dataset is vulnerable to aggregation bias as some variables are collected at a county level, while education data is specific to individual school campuses. The issue arises from assuming that county-level data can adequately represent each campus, whereas in reality, substantial disparities may exist among students' families at different campuses within the same county. Concerning this issue, improving our dataset involves gathering data at the school district or campus level for temperature and census information, which can subsequently enhance the accuracy of causal effect assessments.

In addition, the presence of outliers in the academic performance variable was identified and has raised concerns regarding the validity of these extreme values. In our opinion, it is highly improbable for every student in a specific campus to either excel or perform poorly. Consequently, our dataset can be improved by a thorough examination and investigation of these extreme values. However, for the purposes of this analysis, these extreme values have been retained without modification.

Finally, we've constructed our database and conducted regression analysis using the overall percentage of students meeting the grade level. It's important to note that the causal effects of our explanatory variables may differ if we were to segregate our academic data by demographics, such as sex, race, or economically disadvantaged students. While this data is accessible, we have chosen not to include it in our analysis. Enhancing the database and analysis involves the incorporation of disaggregated academic performance variables.

Analysis:

The dataset contains observational data, so we should be careful when making conclusions about causation between the dependent and independent variables in the regression analysis. The results may be affected by various problems that could create bias, even though we included several control variables in the regression. It's possible that we left out important confounding factors that could affect our model and cause our results to be biased. Some of the potential missing variables that could affect the results include institutional factors, school resources, additional family-related factors, and teaching practices. Accessing quasi-experimental or experimental data in this field comes at a high cost. However, incorporating the variables mentioned earlier can lead to bias reduction and more accurate causal identification.

# Conclusion

In this project, we explored the impact of teacher quality, temperature, and census variables on student academic performance. We sourced our data from three distinct providers: Texas Education Agency (TEA), Southern Regional Climate Center (SRCC) and  American Community Survey 5-Year. We used Python to script the extraction of data from these sources and integrated it into our dataset. Following that, scatter plots were developed to investigate the relationship between each variable and student academic performance across various courses, and then we picked up 8 most relevant variables to do regression analysis. From this analysis, we identified 8 highly relevant variables for regression analysis. Our findings reveal that, across all four subjects (English, US History, Biology, and Math), class size, teacher experience, and teacher degree have a significant positive influence on high student academic performance. Furthermore, we observed that average minimum temperature slightly affects students' US history grades negatively, and the poverty rate negatively impacts students' performance in Biology, English, and US history. With respect to database limitations, first, our data collection was conducted at various levels, with education data obtained at the campus level and other data collected at the county level. We made the assumption that county-level data can sufficiently represent each individual campus. Additionally, we did not perform outlier removal in the academic performance data. It's worth noting that there are inherent limitations in our dataset, and we didn't thoroughly examine the causal effects of our explanatory variables. 













