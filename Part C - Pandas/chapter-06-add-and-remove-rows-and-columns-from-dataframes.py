import pandas as pd

df = pd.read_csv("Part C - Pandas/data/survey_results_public.csv", index_col = "Respondent")

print(df.head())

# 1. Below you will find information for a new row. Add it to the survey DataFrame.
new_row = {
            "MainBranch": "I am a student who is learning to code", 
            "Hobbyist": "Yes",
            "OpenSourcer": "Once a month or more often",
            "Employment": "Employed part-time",
            "Country": "Germany",
            "Student": "Yes, full-time"
          }

# df = df.append(new_row, ignore_index=True) gives error!

new_row_df = pd.DataFrame([new_row])

df = pd.concat([df, new_row_df], ignore_index=True)

print(df.tail())

# 2. Below you will find three columns that appear to contain many NaN values. Remove these columns from the survey DataFrame.
columns_drop = ["BlockchainOrg", "CodeRevHrs", "ConvertedComp"]

df.drop(labels = columns_drop, axis = "columns", inplace = True)

assert "BlockchainOrg" not in df.columns, "As it seems you did not drop the BlockchainOrg column."
assert "CodeRevHrs" not in df.columns, "As it seems you did not drop the CodeRevHrs column."
assert "ConvertedComp" not in df.columns, "As it seems you did not drop the ConvertedComp column."

# 3. Drop every survey respondent who is not resident in the US.
# DEFINE A FILTER HERE.
filt = ~(df["Country"] == "United States")

# DROP THE ROWS HERE.
df.drop(labels = df.loc[filt].index, axis = "rows", inplace = True)

assert len(df["Country"].unique()) == 1, "Your filter seems to not work!"
assert df["Country"].unique()[0] == "United States", "You did not extract residents from the US!"
