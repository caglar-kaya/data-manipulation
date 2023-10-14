# 1. In the following tasks, we will work with an e-commerce dataset from the Kaggle platform (https://www.kaggle.com/carrie1/ecommerce-data). 
# This dataset is stored under data/transaction_details.csv and contains transaction details of an online store from the end of 2010 to the end of 2011. 
# First, the dataset has to be loaded. Thereby, four parameters of the read_csv method have to be adjusted: sep, na_values, parse_dates, and date_parser. 
# After the dataset has been loaded, all rows should be removed where both the CustomerID and Description column contain NaN values. 
# The DataFrame should be saved as df.

import pandas as pd
from datetime import datetime
import numpy as np

df = pd.read_csv("Part C - Pandas/data/transaction_details.csv", sep = ";", na_values = "MISSING_DATA",
               parse_dates= ["InvoiceDate"], date_format="%m/%d/%Y %H:%M")

df.dropna(how = "all", subset = ["Description", "CustomerID"], inplace = True)

print(df.head(10))

assert df.shape == (540455, 8), "Your DataFrame seems to have the wrong shape!"
assert np.dtype('<M8[ns]') == df["InvoiceDate"].dtype, "The InvoiceDate column should contain DateTime objects!"

# 2. Calculate the revenue during January in 2011 and store it in a variable named revenue_january.

df["OverallPrice"] = df["Quantity"] * df["UnitPrice"]
revenue_january = df.set_index("InvoiceDate").loc["2011-01", "OverallPrice"].sum()

assert revenue_january == 560000.2599999999, "Your result seems to be incorrect!"

# 3. In which month during 2011 was the revenue the most? Store this month's name as a String (i.e., January) in a variable named revenue_month.

revenue_month = df.set_index("InvoiceDate").loc[:, "OverallPrice"].resample("M").sum().idxmax().month_name()

assert revenue_month == "November", "Your result seems to be incorrect!"

# 4. From which country did the most orders come in November 2011? Store this country's name as a String (i.e., United States) called country_orders.

country_orders = df.set_index("InvoiceDate").loc["2011-11", "Country"].value_counts().idxmax()

assert country_orders == "United Kingdom", "Your result seems to be incorrect!"
