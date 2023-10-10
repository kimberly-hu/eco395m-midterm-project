import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy.stats import linregress


def float_(df):
    """Create a list of float type variables in a data frame"""

    float_list = df.select_dtypes(include=["float"]).columns.tolist()

    return float_list


def summ_stats(df):
    """Create a summary table for all float variables in a data frame"""

    statistics_list = []
    float_list = float_(df)

    for var in float_list:
        min_val = df[var].min()
        max_val = df[var].max()
        mean_val = df[var].mean()
        median_val = df[var].median()
        percentile_25 = df[var].quantile(0.25)
        percentile_75 = df[var].quantile(0.75)
        count_of_0 = (df[var] == 0).sum()
        count_of_NA = df[var].isna().sum()

        statistics_list.append(
            {
                "Variable": var,
                "Min": min_val,
                "Max": max_val,
                "Mean": mean_val,
                "Median": median_val,
                "25th_Percentile": percentile_25,
                "75th_Percentile": percentile_75,
                "Count_of_0": count_of_0,
                "Count_of_NA": count_of_NA,
            }
        )

    statistics_df = pd.DataFrame(statistics_list)

    return statistics_df


data_path = "data"
output_path = "artifacts"


all_data = pd.read_csv(os.path.join(data_path, "all_data.csv"))
summ_df = summ_stats(all_data)
summ_df.to_csv(os.path.join(output_path,"summary_statistics.csv"), index=False)



def gen_scatter_plots(df, str, path):
    """Generate scatter plots for str and x variables"""
    y = df[f"{str}"]

    x_vars = [
        "Class_Size_Math",
        "Class_Size_English",
        "Class_Size_Sci",
        "Class_Size_Soc_Stud",
        "Teacher_Beginning_Percent",
        "Teacher_1-5_Years_Percent",
        "Teacher_6-10_Years_Percent",
        "Teacher_11-20_Years_Percent",
        "Teacher_More_Than_20_Years_Percent",
        "Teacher_BA_Degree_Percent",
        "Teacher_Experience_Average",
        "Teacher_Student_Ratio",
        "Teacher_MS_Degree_Percent",
        "Teacher_No_Degree_Percent",
        "Teacher_PH_Degree_Percent",
        "Teacher_Tenure_Average",
        "Median_Household_Income",
        "Gini_Index",
        "Median_Family_Income",
        "Poverty_Rate",
        "Avg_Max_Temp",
        "Avg_Min_Temp",
    ]

    for x_var in x_vars:
        x = all_data[x_var]

        mask = ~x.isnull() & ~y.isnull()
        x_cleaned = x[mask]
        y_cleaned = y[mask]

        if len(x_cleaned) == 0 or len(y_cleaned) == 0:
            continue

        plt.scatter(x_cleaned, y_cleaned, alpha=0.3)
        plt.xlabel(x_var)
        plt.ylabel(str)
        plt.title(f"Scatter Plot: {str} vs. {x_var}")

        sns.regplot(
            x=x_cleaned,
            y=y_cleaned,
            scatter=False,
            color="red",
            label="Regression Line",
        )

        slope, intercept, r_value, p_value, std_err = linregress(x_cleaned, y_cleaned)

        plt.text(x_cleaned.min(), y_cleaned.max(), f"Slope: {slope:.1f}", fontsize=12)
        plt.text(
            x_cleaned.min(),
            y_cleaned.max() - (y_cleaned.max() - y_cleaned.min()) * 0.05,
            f"Intercept: {intercept:.1f}",
            fontsize=12,
        )

        output_file = os.path.join(path, f"{str}_vs_{x_var}.png")

        plt.savefig(output_file)

        plt.clf()


bio_path = os.path.join(output_path,"scatter_plots","Scatter_Biology")
alg_path = os.path.join(output_path,"scatter_plots","Scatter_Algebra")

gen_scatter_plots(all_data, "Algebra_Rate", alg_path)
gen_scatter_plots(all_data, "Biology_Rate", bio_path)