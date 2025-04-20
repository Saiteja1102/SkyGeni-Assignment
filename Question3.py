# What was the average inflation rate when their subscriptions were renewed?

import pandas 

# import csv files and makes the dates into dates format
subscription_information_table = pandas.read_csv("subscription_information.csv", parse_dates=["start_date", "end_date"])
finanical_information_table = pandas.read_csv("finanical_information.csv", parse_dates=["start_date", "end_date"])

# Function to get inflation rate for a specific date
def get_inflation(date):
    row = finanical_information_table[
        (finanical_information_table['start_date'] <= date) &
        (finanical_information_table['end_date'] >= date)
    ]
    return row['inflation_rate'].values[0] if not row.empty else None

# Appling inflation for start dates and end dates
subscription_information_table["inflation_start"] = subscription_information_table["start_date"].apply(get_inflation)
subscription_information_table["inflation_end"] = subscription_information_table["end_date"].apply(get_inflation)

# Filter only renewed subscriptions
renewed_subs = subscription_information_table[subscription_information_table["renewed"] == True]

# Calculate average inflation
average_inflation = ((renewed_subs["inflation_start"] + renewed_subs["inflation_end"]) / 2).mean()
print("Average Inflation Rate: ", average_inflation)
