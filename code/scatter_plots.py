import matplotlib.pyplot as plt
import pandas as pd

all_data = pd.read_csv("data/all_data.csv")
#print(all_data.dtypes)


# English rate and class size

x = all_data['Class_Size_English']
y = all_data['English_Rate']

plt.scatter(x, y, alpha=0.5)

# Add labels and a title
plt.xlabel('Class_Size_English')
plt.ylabel('English_Rate')
plt.title('Scatter Plot: English_Rate vs. Class_Size_English')

plt.savefig('artifacts/scatter_plots/English_vs_Class_Size_English.png')
plt.clf()

# English rate and average teaching experience

x = all_data['Teacher_Experience_Average']
y = all_data['English_Rate']

plt.scatter(x, y, alpha=0.5)

# Add labels and a title
plt.xlabel('Teacher_Experience_Average')
plt.ylabel('English_Rate')
plt.title('Scatter Plot: English_Rate vs. Teacher_Experience_Average')

plt.savefig('artifacts/scatter_plots/English_vs_Teacher_Experience_Average.png')
plt.clf()