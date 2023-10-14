import pandas as pd
import numpy as np

df = pd.read_csv("Part C - Pandas/data/survey_results_public.csv", index_col = "Respondent")

print(df.head(10))

# 1. Create an overview of the coding experience ("YearsCode" column; mean) and the compensation ("ConvertedComp"; median) per country.
# To do so, change the data type from the "YearsCode" column to float (replace "Less than 1 year" with 0 and "More than 50 years" with 51).
# Please return a DataFrame named country_overview

df["YearsCode"].replace("Less than 1 year", 0, inplace = True)
df["YearsCode"].replace("More than 50 years", 51, inplace = True)
df["YearsCode"] = df["YearsCode"].astype(float)
groupby_object = df.groupby("Country")
country_overview = groupby_object.agg({"YearsCode": "mean", "ConvertedComp": "median"})

assert type(country_overview) == type(pd.DataFrame([])), "Please return a DataFrame!"
assert country_overview.loc["Germany", "YearsCode"] == 12.784108460614382, "Your results seem to be incorrect!"
assert country_overview.loc["United States", "ConvertedComp"] == 110000.0, "Your results seem to be incorrect!"
assert country_overview.loc["India", "ConvertedComp"] == 10080.0, "Your results seem to be incorrect!"

# 2. Create an overview that shows what percentage of respondents are very satisfied ("JobSat" column) with their current job per country ("Country" column). 
# Return a Series object named satisfied_percentage that is sorted in descending order.

# This drops every participant that did not answer both questions.
task_df = df[["JobSat", "Country"]].dropna()

groupby_object = task_df.groupby("Country")
satisfied_per_country = groupby_object["JobSat"].apply(lambda x: (x == "Very satisfied").sum())
respondents_per_country = df["Country"].value_counts()
satisfied_percentage = (satisfied_per_country/respondents_per_country).sort_values(ascending = False)

assert type(satisfied_percentage) == type(pd.Series([], dtype = "int64")), "Please return a Series!"
assert satisfied_percentage.loc["Germany"] == 0.24616433685646097, "Your results seem to be incorrect!"
assert satisfied_percentage.loc["United States"] == 0.3435486180724617, "Your results seem to be incorrect!"
assert satisfied_percentage.loc["India"] == 0.16410992164220284, "Your results seem to be incorrect!"

# 3. The mean is known to be strongly influenced by outliers. 
# Therefore, create an overview showing how many participants per country receive a higher compensation (ConvertedComp column) than the respective country average. 
# Contrast this column with how many people from each country (Country column) generally participated in the study. 
# The first line of code is already given to include only participants that answered both questions. 
# Please return a DataFrame named comp_average.

# This drops every participant that did not answer both questions.
comp_average = df[["Country", "ConvertedComp"]].dropna()

country_mean = df.groupby("Country").agg({"ConvertedComp": "mean"})
comp_average["above_average"] = [compensation > country_mean.loc[country, "ConvertedComp"]
                            for compensation, country in zip(comp_average["ConvertedComp"].values,
                            comp_average["Country"].values)]
comp_average = comp_average.groupby(
    "Country").agg({"above_average": "sum", "Country": "count"}).rename(
    {"above_average": "Number of respondents with an above average compensation",
     "Country": "Total number of respondents"}, axis = 1)

assert type(comp_average) == type(pd.DataFrame([])), "Please return a DataFrame!"
assert comp_average.shape == (161, 2), "Your DataFrame seems to have the wrong dimensions!"
assert np.array_equal(comp_average.loc["United States"].to_numpy(), [1911, 14981]), "Your results seem to be wrong!"
assert np.array_equal(comp_average.loc["Germany"].to_numpy(), [466, 3778]), "Your results seem to be wrong!"
assert np.array_equal(comp_average.loc["India"].to_numpy(), [677, 3999]), "Your results seem to be wrong!"
