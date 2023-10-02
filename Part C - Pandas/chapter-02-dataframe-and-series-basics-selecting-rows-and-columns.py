import pandas as pd

df = pd.read_csv("Part C - Pandas/data/survey_results_public.csv")

print(df.head(10))

# 1. Grab the 20th column and the 20th row from the survey dataset.
column_20 = df.iloc[:, 19]
row_20 = df.iloc[19, :]

assert column_20.iloc[2] == "Not sure", "It seems as you picked the wrong column!"
assert row_20["Hobbyist"] == "No", "It seems as you picked the wrong row!"

# 2. Grab the 10th, 500th, and 4500th row as well as the columns EdLevel, CompTotal, and CodeRevHrs from the survey dataset.
index_df = df.loc[[9, 499, 4499], ['EdLevel', 'CompTotal', 'CodeRevHrs']]

assert index_df.iloc[0, -1] == 4.0, "It seems as you filtered the wrong rows/columns!"

# 3. Grab the first hundred rows, as well as the columns between Hobbyist and Student (both including) from the survey dataset.
index_df = df.loc[:99, "Hobbyist":"Student"]

assert index_df.loc[0, "Country"] == "United Kingdom", "It seems as you filtered the wrong rows/columns!"
