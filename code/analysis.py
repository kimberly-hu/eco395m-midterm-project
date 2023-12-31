import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from scipy.stats import linregress
import statsmodels.api as sm


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
summ_df.to_csv(os.path.join(output_path, "summary_statistics.csv"), index=False)


def gen_scatter_plots(df, str, path):
    """Generate scatter plots for str variable and x variables"""
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


bio_path = os.path.join(output_path, "scatter_plots", "Scatter_Biology")
alg_path = os.path.join(output_path, "scatter_plots", "Scatter_Algebra")
eng_path = os.path.join(output_path, "scatter_plots", "Scatter_English")
hist_path = os.path.join(output_path, "scatter_plots", "Scatter_History")

gen_scatter_plots(all_data, "Algebra_Rate", alg_path)
gen_scatter_plots(all_data, "Biology_Rate", bio_path)
gen_scatter_plots(all_data, "English_Rate", eng_path)
gen_scatter_plots(all_data, "US_History_Rate", hist_path)


corr_output_path = os.path.join(output_path, "correlations")


corr_variables_english = all_data[
    [
        "English_Rate",
        "Avg_Max_Temp",
        "Avg_Min_Temp",
        "Class_Size_English",
        "Teacher_Experience_Average",
        "Teacher_MS_Degree_Percent",
        "Median_Household_Income",
        "Gini_Index",
        "Poverty_Rate",
    ]
]

corr_variables_english = corr_variables_english.dropna()
correlation_matrix_english = corr_variables_english.corr()

plt.rc("font", size=6)
plt.figure(figsize=(9.5, 8.5))
plt.title("Correlation Table: English", fontsize=12)
sns.heatmap(correlation_matrix_english, annot=True, cmap="coolwarm")
plt.savefig(f"{corr_output_path}/correlation_matrix_english.png", dpi=300)
plt.close()


corr_variables_math = all_data[
    [
        "Algebra_Rate",
        "Avg_Max_Temp",
        "Avg_Min_Temp",
        "Class_Size_Math",
        "Teacher_Experience_Average",
        "Teacher_MS_Degree_Percent",
        "Median_Household_Income",
        "Gini_Index",
        "Poverty_Rate",
    ]
]

corr_variables_math = corr_variables_math.dropna()
correlation_matrix_math = corr_variables_math.corr()

plt.rc("font", size=6)
plt.figure(figsize=(9.5, 8.5))
plt.title("Correlation Table: Math", fontsize=12)
sns.heatmap(correlation_matrix_math, annot=True, cmap="coolwarm")
plt.savefig(f"{corr_output_path}/correlation_matrix_math.png", dpi=300)
plt.close()


corr_variables_sci = all_data[
    [
        "Biology_Rate",
        "Avg_Max_Temp",
        "Avg_Min_Temp",
        "Class_Size_Sci",
        "Teacher_Experience_Average",
        "Teacher_MS_Degree_Percent",
        "Median_Household_Income",
        "Gini_Index",
        "Poverty_Rate",
    ]
]

corr_variables_sci = corr_variables_sci.dropna()
correlation_matrix_sci = corr_variables_sci.corr()

plt.rc("font", size=6)
plt.figure(figsize=(9.5, 8.5))
plt.title("Correlation Table: Biology", fontsize=12)
sns.heatmap(correlation_matrix_sci, annot=True, cmap="coolwarm")
plt.savefig(f"{corr_output_path}/correlation_matrix_sci.png", dpi=300)
plt.close()


corr_variables_soc_stud = all_data[
    [
        "US_History_Rate",
        "Avg_Max_Temp",
        "Avg_Min_Temp",
        "Class_Size_Soc_Stud",
        "Teacher_Experience_Average",
        "Teacher_MS_Degree_Percent",
        "Median_Household_Income",
        "Gini_Index",
        "Poverty_Rate",
    ]
]

corr_variables_soc_stud = corr_variables_soc_stud.dropna()
correlation_matrix_soc_stud = corr_variables_soc_stud.corr()

plt.rc("font", size=6)
plt.figure(figsize=(9.5, 8.5))
plt.title("Correlation Table: US History", fontsize=12)
sns.heatmap(correlation_matrix_soc_stud, annot=True, cmap="coolwarm")
plt.savefig(f"{corr_output_path}/correlation_matrix_soc_stud.png", dpi=300)
plt.close()


OLS_algebra = sm.OLS(
    endog=all_data["Algebra_Rate"],
    exog=sm.add_constant(all_data.iloc[:, [41, 42, 6, 21, 24, 37, 38, 40]]),
    missing="drop",
).fit()

OLS_biology = sm.OLS(
    endog=all_data["Biology_Rate"],
    exog=sm.add_constant(all_data.iloc[:, [41, 42, 7, 21, 24, 37, 38, 40]]),
    missing="drop",
).fit()

OLS_english = sm.OLS(
    endog=all_data["English_Rate"],
    exog=sm.add_constant(all_data.iloc[:, [41, 42, 5, 21, 24, 37, 38, 40]]),
    missing="drop",
).fit()

OLS_history = sm.OLS(
    endog=all_data["US_History_Rate"],
    exog=sm.add_constant(all_data.iloc[:, [41, 42, 8, 21, 24, 37, 38, 40]]),
    missing="drop",
).fit()

results_algebra = OLS_algebra.summary()
algebra_csv = results_algebra.as_csv()
with open("artifacts/regressions/OLS_results_algebra.csv", "w") as f:
    f.write(algebra_csv)

results_biology = OLS_biology.summary()
biology_csv = results_biology.as_csv()
with open("artifacts/regressions/OLS_results_biology.csv", "w") as f:
    f.write(biology_csv)

results_english = OLS_english.summary()
english_csv = results_english.as_csv()
with open("artifacts/regressions/OLS_results_english.csv", "w") as f:
    f.write(english_csv)

results_history = OLS_history.summary()
history_csv = results_history.as_csv()
with open("artifacts/regressions/OLS_results_history.csv", "w") as f:
    f.write(history_csv)
