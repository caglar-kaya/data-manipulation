import pandas as pd

df = pd.read_csv("Part C - Pandas/data/survey_results_public.csv")

print(df.head(10))

# 1. What are the dimensions of our survey DataFrame? How many rows, how many columns do we have?
rows = df.shape[0]
columns = df.shape[1]

print("Our survey data has {} rows and {} columns.".format(rows, columns))

# 2. Five columns have the datatype float64: Which are those?
# Add the respective column names to this list as strings.
dtypes_series = df.dtypes

float64_columns = dtypes_series[dtypes_series == 'float64'].index.tolist()

print("The following columns have the data type float64: ", " ,".join(float64_columns))

# 3. Return the last 10 rows of the survey DataFrame.
last_10_rows = df.tail(10)

print(last_10_rows)
