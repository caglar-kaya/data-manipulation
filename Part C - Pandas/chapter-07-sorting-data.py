import pandas as pd

df = pd.read_csv("Part C - Pandas/data/survey_results_public.csv", index_col = "Respondent")

print(df.head(10))

# 1. Filter out the 15 respondents with the most coding experience ("YearsCode" column) that live in Germany ("Country" column).
# To do so, change the data type from the "YearsCode" column to float (replace "Less than 1 year" with 0 and "More than 50 years" with 51; read hints for further explanation).
# Please return a list named most_experience that contains tuples as elements in the format of (respondent id, coding experience). 
# This list should be in decreasing order with regard to the coding experience.

df["YearsCode"].replace("Less than 1 year", 0, inplace = True)
df["YearsCode"].replace("More than 50 years", 51, inplace = True)
df["YearsCode"] = df["YearsCode"].astype(float)
filt = (df["Country"] == "Germany")
filt_df = df.loc[filt]
filt_series = filt_df["YearsCode"].nlargest(15)
most_experience = [(index, experience) for index, experience in zip(filt_series.index, filt_series.values)]

assert len(most_experience) == 15, "Please return 15 respondents!"
assert most_experience[0] == (31522, 51), "Your results seem to be incorrect!"
assert most_experience[10] == (27999, 44), "Your results seem to be incorrect!"
assert most_experience[-1] == (55887, 43), "Your results seem to be incorrect!"

# 2. What are the ten highest salaries in Germany (ConvertedComp column)? 
# Please return a Series named largest_10 whose index contains respondent ids and whose values specify the compensation.

filt = (df["Country"] == "Germany")
series_filt = df.loc[filt, "ConvertedComp"]
largest_10 = series_filt.nlargest(10)

assert type(largest_10) == type(pd.Series([], dtype = "int64")), "Please return a Series!"
assert largest_10.iloc[0] == 2000000, "Your sorting does not seem to work!"
assert (largest_10.iloc[1:] == 1000000).unique() == True, "Your sorting does not seem to work!"

# 3. The highest reported salary appears to be 2000000 USD per year (ConvertedComp column). 
# As someone's salary is not necessarily linked to their working hours per week (WorkWeekHrs column), 
# we want to determine the least amount of work required to earn such high figures. 
# Please return a Series named smallest_10 containing the ten lowest working hours per week for respondents who have reported earning 2000000 USD per year. 
# Its index refers to the respondent ids, and its values specify the working hours per week.

filt = (df["ConvertedComp"] == 2000000)
series_filt = df.loc[filt, "WorkWeekHrs"]
smallest_10 = series_filt.nsmallest(10)

assert type(smallest_10) == type(pd.Series([], dtype = "int64")), "Please return a Series!"
assert smallest_10.iloc[0] == 2, "Your sorting does not seem to work!"
assert smallest_10.iloc[5] == 24, "Your sorting does not seem to work!"
