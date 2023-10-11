import pandas as pd

df = pd.read_csv("Part C - Pandas/data/survey_results_public.csv", index_col = "Respondent")

print(df.head(10))

# 1. The survey DataFrame's index ranges from 1 to n, where n corresponds to the number of survey participants. 
# Drop every row from the DataFrame where the questions Country, YearsCode, and ConvertedComp have not been answered. 
# Do not make this drop in place but instead assign the cleaned DataFrame to a new variable named cleaned_df. 
# Your final goal is to store the dropped indexes (i.e., 2679, 4271, etc.) in a list called dropped_indexes.

cleaned_df = df.dropna(axis = 0, how = "all", subset = ["Country", "YearsCode", "ConvertedComp"])
dropped_indexes = [index for index in df.index if index not in cleaned_df.index]

assert cleaned_df.shape == (88751, 84), "Your drop seems to be incorrect!"
assert len(dropped_indexes) == 132, "Your dropped_indexes list seems to have the wrong length!"
assert 12032 in dropped_indexes, "Your dropped_indexes list does not contain every index!"
assert 57311 in dropped_indexes, "Your dropped_indexes list does not contain every index!"
assert 73522 in dropped_indexes, "Your dropped_indexes list does not contain every index!"
assert 88802 in dropped_indexes, "Your dropped_indexes list does not contain every index!"

# 2. On average, when did participants write their first line of code (Age1stCode column)? 
# To answer this question, replace "younger than" and "older than" statements within the YearsCode column with the nearest age. 
# For example, "older than 45" would become 46. Store the mean in a variable named mean_age_code.

df["Age1stCode"].replace("Younger than 5 years", 4, inplace = True)
df["Age1stCode"].replace("Older than 85", 86, inplace = True)
df["Age1stCode"] = df["Age1stCode"].astype(float)
mean_age_code = df["Age1stCode"].mean()

assert df["Age1stCode"].dtype == float, "You need to change the column's data type!"
assert round(mean_age_code, 2) == 15.41, "Your result seems to be incorrect!"
assert len(str(mean_age_code)) == 18, "Your result seems to be incorrect!"
