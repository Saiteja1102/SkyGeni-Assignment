# What is the median amount paid each year for all payment methods?

# Importing pandas library
import pandas

# import payment_information.csv file and convert dates into dates type
payment_information_table = pandas.read_csv("payment_information.csv",parse_dates=["payment_date"])

# Adding year column
payment_information_table["year"] = payment_information_table["payment_date"].dt.year
# Grouping by Year
median_per_year_groupby = payment_information_table.groupby("year")
# Finding median
median_per_year = median_per_year_groupby["amount_paid"].median()
# Print
print(median_per_year)

import matplotlib.pyplot as plt

# Plotting median amount paid per year
median_per_year.plot(kind='line', marker='o', color='blue')
plt.title("Median Amount Paid Per Year")
plt.xlabel("Year")
plt.ylabel("Median Amount Paid")
plt.tight_layout()
plt.show()
