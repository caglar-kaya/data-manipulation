import pandas as pd

df = pd.read_csv("Part C - Pandas/data/survey_results_public.csv", index_col = "Respondent")

print(df.head(10))

# 1. Adjust the DataFrame's column names so that every column name is lowercased.
old_columns = df.columns
print(old_columns)

df.columns = [x.lower() for x in df.columns]
print(df.columns)

assert df.columns[0] == "mainbranch", "Your lowercasing does not seem to work!"
assert df.columns[-1] == "surveyease", "Your lowercasing does not seem to work!"

# For better readability, we undo this change. We applied it just for practice reasons. 
df.columns = old_columns
print(df.columns)

# 2. Some column names are misleading. Rename the columns CareerSat and MgrIdiot to CareerSatisfaction and ManagerAwareness.
df.rename(columns = {'CareerSat': 'CareerSatisfaction', 'MgrIdiot': 'ManagerAwareness'}, inplace = True)

assert "CareerSatisfaction" in df.columns, "You did not rename CareerSat correctly!"
assert "ManagerAwareness" in df.columns, "You did not rename MgrIdiot correctly!"

# 3. For comparison reasons, we want to convert the current dollar salaries to euro salaries (CompTotal column). 
# At that, we assume an exchange ratio of 85%. 
# Therefore, one dollar should equal 85 cents.
df["CompTotal"] = df["CompTotal"].apply(lambda x: x * 0.85)

assert df["CompTotal"].loc[3] == 19550, "Your conversion does not seem to work properly!"
assert df["CompTotal"].loc[10] == 807500, "Your conversion does not seem to work properly!"
assert df["CompTotal"].loc[20] == 2550, "Your conversion does not seem to work properly!"

#4. In the OpenSourcer column, respondents were asked how often they contribute to open source projects. 
# The answer options were: "Never," "Less than once per year," "Less than once a month but more than once per year," and "Once a month or more often." 
# Complete the adjust_OpenSourcer-function so that it can be applied to the OpenSourcer column. 
# The goal is for the new OpenSourcer column to contain False (boolean) if a respondent answered "Never". Otherwise, it should contain True (boolean).
def adjust_OpenSourcer(answer):
    if answer == 'Never':
        return False
    else:
        return True
    
df["OpenSourcer"] = df["OpenSourcer"].apply(adjust_OpenSourcer)

assert df["OpenSourcer"].dtype == "bool", "adjust_OpenSourcer shall return boolean values!"
assert df["OpenSourcer"].iloc[0] == False, "Your adjustment seems to be incorrect!"
assert df["OpenSourcer"].iloc[-1] == True, "Your adjustment seems to be incorrect!"
