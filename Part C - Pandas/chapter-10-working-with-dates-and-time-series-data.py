import pandas as pd
from datetime import datetime
import numpy as np

df = pd.read_csv("Part C - Pandas/data/ETH_1h.csv", parse_dates=["Date"], date_format="%Y-%m-%d %I-%p")

print(df.head(10))

# 1. On which day in December 2018 Ethereum reached had its highest closing price?
# Use the mean to average the hourly data points. 
# Store the day as a String in a variable named closing_day.

desired_period = df.set_index(["Date"]).loc["2018-12", "Close"].resample("D").mean()
closing_day = desired_period.idxmax().day_name()

assert closing_day == "Monday", "Your result seems to be incorrect!"

# 2. At what month in 2019 Ethereum had the highest closing price? 
# Use the mean to average the hourly data points. 
# Store the month as a String in a variable named closing_month.

desired_period = df.set_index(["Date"]).loc["2019", "Close"].resample("M").mean()
month_closing = desired_period.idxmax().month_name()

assert month_closing == "June", "Your result seems to be incorrect!"

# 3. On which days between 2017 and 2020 did Ethereum have the lowest and highest price? 
# Use the mean to average the hourly data points and calculate the time delta between these two dates. 
# Store timedelta as a Timedelta object in a variable named timedelta.

filt = (df["Date"] > "2017") & (df["Date"] < "2020")
desired_period = df.loc[filt, ["High", "Low", "Date"]].set_index(["Date"]).resample("D").mean()
timedelta = np.abs(desired_period["High"].idxmax()-desired_period["Low"].idxmin())

assert type(timedelta) == type(pd.Timedelta(1)), "Please return a Timedelta object!"
assert np.abs(timedelta.days) == 335, "Your timedelta seems to be incorrect!"
