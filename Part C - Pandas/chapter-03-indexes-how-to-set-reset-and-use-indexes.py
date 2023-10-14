import pandas as pd

df = pd.read_csv("Part C - Pandas/data/survey_results_public.csv")

print(df.head(10))

# 1. Above, we load the DataFrame without specifying an index column. As the Respondent column can serve as an index, set this column as the index.
df.set_index(keys = "Respondent", inplace = True)

assert df.index.name == "Respondent", "It seems as you set the wrong column as the index!"

# 2. Grab the 10th, 500th, and 4500th row as well as the columns EdLevel, CompTotal, and CodeRevHrs from the survey dataset.
index_df = df.loc[[10, 500, 4500], ['EdLevel', 'CompTotal', 'CodeRevHrs']]

assert index_df.iloc[0, -1] == 4.0, "It seems as you filtered the wrong rows/columns!"

# 3. Grab the first hundred rows, as well as the columns between Hobbyist and Student (both including) from the survey dataset.
index_df = df.loc[1:100, 'Hobbyist':'Student']

assert index_df.loc[1, "Country"] == "United Kingdom", "It seems as you filtered the wrong rows/columns!"
