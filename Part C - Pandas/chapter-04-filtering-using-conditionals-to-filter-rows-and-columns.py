import pandas as pd

df = pd.read_csv("Part C - Pandas/data/survey_results_public.csv", index_col = "Respondent")

print(df.head(10))

# 1. Filter out all respondents with total compensation of more than 100,000 USD per year (CompTotal column). 
# We are only interested in the country in which they lived when completing the survey (Country column). 
# Then create an overview that shows the number of high earners per country. 
# filt_overview should be a Series with countries as its index and compensation counts as its values.

# DEFINE A FILTER HERE.
filt = (df['CompTotal'] > 100000)

# APPLY THE FILTER HERE.
df_filt = df.loc[filt, 'Country']
print(df_filt)

# EXTRACT COUNTS PER COUNTRY HERE.
filt_overview = df_filt.value_counts()
print(filt_overview)

assert type(filt_overview) == type(pd.Series([], dtype = "int64")), "Please return a Series!"
assert filt_overview.loc["United States"] == 7615, "Your count for the US does not seem to be correct!"
assert filt_overview.loc["Australia"] == 573, "Your count for Australia does not seem to be correct!"
assert filt_overview.shape[0] == 128, "Your filter does not seem to work correctly!"

# 2. Filter out all respondents with total compensation greater than 100,000 USD per year who are also US residents. 
# We are interested in how coding experience is distributed along these (YearsCode column). 
# Therefore, create an overview that indicates how many of those developers have how many years of experience. 
# filt_overview should be a Series with years of coding experience as its index and developer counts as its values.

# DEFINE A FILTER HERE.
filt = (df['CompTotal'] > 100000) & (df['Country'] == 'United States')

# APPLY THE FILTER HERE.
df_filt = df.loc[filt, 'YearsCode']
print(df_filt)

# EXTRACT COUNTS PER YEARS OF EXPERIENCE HERE.
filt_overview = df_filt.value_counts()
print(filt_overview)

assert type(filt_overview) == type(pd.Series([], dtype = "int64")), "Please return a Series!"
assert filt_overview.loc["20"] == 636, "Your count for 20 years of experience does not seem to be correct!"
assert filt_overview.loc["40"] == 118, "Your count for 40 years of experience does not seem to be correct!"
assert filt_overview.shape[0] == 52, "Your filter does not seem to work correctly!"

# 3. Filter out all respondents with total compensation greater than 100,000 USD per year who are not residents in the US, India, Canada, Russia, or Australia. 
# Then create an overview that shows the number of high earners per country. 
# filt_overview should be a Series with countries as its index and compensation as its values.

countries = ["United States", "India", "Canada", "Russian Federation", "Australia"]

# DEFINE A FILTER HERE.
filt = (df['CompTotal'] > 100000) & (~df['Country'].isin(countries))

# APPLY FILTER HERE.
df_filt = df.loc[filt, 'Country']
print(df_filt)

# EXTRACT COUNTS PER COUNTRY HERE.
filt_overview = df_filt.value_counts()
print(filt_overview)

assert type(filt_overview) == type(pd.Series([], dtype = "int64")), "Please return a Series!"
assert filt_overview.loc["Iran"] == 393, "Your count for Iran does not seem to be correct!"
assert filt_overview.loc["United Kingdom"] == 230, "Your count for the United Kingdom does not seem to be correct!"
assert filt_overview.shape[0] == 123, "Your filter does not seem to work correctly!"
