import matplotlib.pyplot as plt
import pandas as pd

all_data = pd.read_csv("data/all_data.csv")
#print(all_data.dtypes)


# English_Rate and Class_Size_English

x = all_data['Class_Size_English']
y = all_data['English_Rate']

plt.scatter(x, y, alpha=0.5)

# Add labels and a title
plt.xlabel('Class_Size_English')
plt.ylabel('English_Rate')
plt.title('Scatter Plot: English_Rate vs. Class_Size_English')

plt.savefig('artifacts/scatter_plots/English_vs_Class_Size_English.png')
plt.clf()




# English_Rate and Teacher_Student_Ratio

x = all_data['Teacher_Student_Ratio']
y = all_data['English_Rate']

plt.scatter(x, y, alpha=0.5)

# Add labels and a title
plt.xlabel('Teacher_Student_Ratio')
plt.ylabel('English_Rate')
plt.title('Scatter Plot: English_Rate vs. Teacher_Student_Ratio')

plt.savefig('artifacts/scatter_plots/English_vs_Teacher_Student_Ratio.png')
plt.clf()




# English_Rate and Teacher_Beginning_Percent

x = all_data['Teacher_Beginning_Percent']
y = all_data['English_Rate']

plt.scatter(x, y, alpha=0.5)

# Add labels and a title
plt.xlabel('Teacher_Beginning_Percent')
plt.ylabel('English_Rate')
plt.title('Scatter Plot: English_Rate vs. Teacher_Beginning_Percent')

plt.savefig('artifacts/scatter_plots/English_vs_Teacher_Beginning_Percent.png')
plt.clf()




# English_Rate and Teacher_1-5_Years_Percent

x = all_data['Teacher_1-5_Years_Percent']
y = all_data['English_Rate']

plt.scatter(x, y, alpha=0.5)

# Add labels and a title
plt.xlabel('Teacher_1-5_Years_Percent')
plt.ylabel('English_Rate')
plt.title('Scatter Plot: English_Rate vs. Teacher_1-5_Years_Percent')

plt.savefig('artifacts/scatter_plots/English_vs_Teacher_1-5_Years_Percent.png')
plt.clf()



# English_Rate and Teacher_6-10_Years_Percent

x = all_data['Teacher_6-10_Years_Percent']
y = all_data['English_Rate']

plt.scatter(x, y, alpha=0.5)

# Add labels and a title
plt.xlabel('Teacher_6-10_Years_Percent')
plt.ylabel('English_Rate')
plt.title('Scatter Plot: English_Rate vs. Teacher_6-10_Years_Percent')

plt.savefig('artifacts/scatter_plots/English_vs_Teacher_6-10_Years_Percent.png')
plt.clf()



# English_Rate and Teacher_11-20_Years_Percent

x = all_data['Teacher_11-20_Years_Percent']
y = all_data['English_Rate']

plt.scatter(x, y, alpha=0.5)

# Add labels and a title
plt.xlabel('Teacher_11-20_Years_Percent')
plt.ylabel('English_Rate')
plt.title('Scatter Plot: English_Rate vs. Teacher_11-20_Years_Percent')

plt.savefig('artifacts/scatter_plots/English_vs_Teacher_11-20_Years_Percent.png')
plt.clf()




# English_Rate and Teacher_More_Than_20_Years_Percent

x = all_data['Teacher_More_Than_20_Years_Percent']
y = all_data['English_Rate']

plt.scatter(x, y, alpha=0.5)

# Add labels and a title
plt.xlabel('Teacher_More_Than_20_Years_Percent')
plt.ylabel('English_Rate')
plt.title('Scatter Plot: English_Rate vs. Teacher_More_Than_20_Years_Percent')

plt.savefig('artifacts/scatter_plots/English_vs_Teacher_More_Than_20_Years_Percent.png')
plt.clf()




# English_Rate and Teacher_Experience_Average

x = all_data['Teacher_Experience_Average']
y = all_data['English_Rate']

plt.scatter(x, y, alpha=0.5)

# Add labels and a title
plt.xlabel('Teacher_Experience_Average')
plt.ylabel('English_Rate')
plt.title('Scatter Plot: English_Rate vs. Teacher_Experience_Average')

plt.savefig('artifacts/scatter_plots/English_vs_Teacher_Experience_Average.png')
plt.clf()



# English_Rate and Teacher_BA_Degree_Percent

x = all_data['Teacher_BA_Degree_Percent']
y = all_data['English_Rate']

plt.scatter(x, y, alpha=0.5)

# Add labels and a title
plt.xlabel('Teacher_BA_Degree_Percent')
plt.ylabel('English_Rate')
plt.title('Scatter Plot: English_Rate vs. Teacher_BA_Degree_Percent')

plt.savefig('artifacts/scatter_plots/English_vs_Teacher_BA_Degree_Percent.png')
plt.clf()




# English_Rate and Teacher_MS_Degree_Percent

x = all_data['Teacher_MS_Degree_Percent']
y = all_data['English_Rate']

plt.scatter(x, y, alpha=0.5)

# Add labels and a title
plt.xlabel('Teacher_MS_Degree_Percent')
plt.ylabel('English_Rate')
plt.title('Scatter Plot: English_Rate vs. Teacher_MS_Degree_Percent')

plt.savefig('artifacts/scatter_plots/English_vs_Teacher_MS_Degree_Percent.png')
plt.clf()




# English_Rate and Teacher_No_Degree_Percent

x = all_data['Teacher_No_Degree_Percent']
y = all_data['English_Rate']

plt.scatter(x, y, alpha=0.5)

# Add labels and a title
plt.xlabel('Teacher_No_Degree_Percent')
plt.ylabel('English_Rate')
plt.title('Scatter Plot: English_Rate vs. Teacher_No_Degree_Percent')

plt.savefig('artifacts/scatter_plots/English_vs_Teacher_No_Degree_Percent.png')
plt.clf()




# English_Rate and Teacher_PH_Degree_Percent

x = all_data['Teacher_PH_Degree_Percent']
y = all_data['English_Rate']

plt.scatter(x, y, alpha=0.5)

# Add labels and a title
plt.xlabel('Teacher_PH_Degree_Percent')
plt.ylabel('English_Rate')
plt.title('Scatter Plot: English_Rate vs. Teacher_PH_Degree_Percent')

plt.savefig('artifacts/scatter_plots/English_vs_Teacher_PH_Degree_Percent.png')
plt.clf()




# English_Rate and Teacher_Tenure_Average

x = all_data['Teacher_Tenure_Average']
y = all_data['English_Rate']

plt.scatter(x, y, alpha=0.5)

# Add labels and a title
plt.xlabel('Teacher_Tenure_Average')
plt.ylabel('English_Rate')
plt.title('Scatter Plot: English_Rate vs. Teacher_Tenure_Average')

plt.savefig('artifacts/scatter_plots/English_vs_Teacher_Tenure_Average.png')
plt.clf()




# English_Rate and Median_Household_Income

x = all_data['Median_Household_Income']
y = all_data['English_Rate']

plt.scatter(x, y, alpha=0.5)

# Add labels and a title
plt.xlabel('Median_Household_Income')
plt.ylabel('English_Rate')
plt.title('Scatter Plot: English_Rate vs. Median_Household_Income')

plt.savefig('artifacts/scatter_plots/English_vs_Median_Household_Income.png')
plt.clf()




# English_Rate and Gini_Index

x = all_data['Gini_Index']
y = all_data['English_Rate']

plt.scatter(x, y, alpha=0.5)

# Add labels and a title
plt.xlabel('Gini_Index')
plt.ylabel('English_Rate')
plt.title('Scatter Plot: English_Rate vs. Gini_Index')

plt.savefig('artifacts/scatter_plots/English_vs_Gini_Index.png')
plt.clf()




# English_Rate and Median_Family_Income

x = all_data['Median_Family_Income']
y = all_data['English_Rate']

plt.scatter(x, y, alpha=0.5)

# Add labels and a title
plt.xlabel('Median_Family_Income')
plt.ylabel('English_Rate')
plt.title('Scatter Plot: English_Rate vs. Median_Family_Income')

plt.savefig('artifacts/scatter_plots/English_vs_Median_Family_Income.png')
plt.clf()




# English_Rate and Poverty_Rate

x = all_data['Poverty_Rate']
y = all_data['English_Rate']

plt.scatter(x, y, alpha=0.5)

# Add labels and a title
plt.xlabel('Poverty_Rate')
plt.ylabel('English_Rate')
plt.title('Scatter Plot: English_Rate vs. Poverty_Rate')

plt.savefig('artifacts/scatter_plots/English_vs_Poverty_Rate.png')
plt.clf()




# English_Rate and Avg_Max_Temp

x = all_data['Avg_Max_Temp']
y = all_data['English_Rate']

plt.scatter(x, y, alpha=0.5)

# Add labels and a title
plt.xlabel('Avg_Max_Temp')
plt.ylabel('English_Rate')
plt.title('Scatter Plot: English_Rate vs. Avg_Max_Temp')

plt.savefig('artifacts/scatter_plots/English_vs_Avg_Max_Temp.png')
plt.clf()




# English_Rate and Avg_Min_Temp

x = all_data['Avg_Min_Temp']
y = all_data['English_Rate']

plt.scatter(x, y, alpha=0.5)

# Add labels and a title
plt.xlabel('Avg_Min_Temp')
plt.ylabel('English_Rate')
plt.title('Scatter Plot: English_Rate vs. Avg_Min_Temp')

plt.savefig('artifacts/scatter_plots/English_vs_Avg_Min_Temp.png')
plt.clf()