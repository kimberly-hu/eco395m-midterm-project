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

