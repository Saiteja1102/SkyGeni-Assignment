# Which industry in the organization has the highest renewal rate?

import pandas # For data Analysis

# Here we are using pandas library to read the csv file i.e to import the file
subscription_information_table = pandas.read_csv("subscription_information.csv")
industry_client_details_table = pandas.read_csv("industry_client_details.csv")

# Joining two tables using Outer join -> Since there is no null values this is perfectly alright
subscription_industry_join = subscription_information_table.merge(industry_client_details_table,on="client_id",how='outer')
# From that we are fecting necessary columns
subscription_industry_join_necessary = subscription_industry_join[["client_id","renewed","industry"]]
# Taking out only True Values
subscription_renewed = subscription_industry_join_necessary[subscription_industry_join_necessary["renewed"] == True]

# Giving names to columns after finding count
subscription_renewed_count = subscription_renewed["industry"].value_counts().reset_index()
subscription_renewed_count.columns = ["industry","renewed_count"]

# Finding the industry with highest renewal rate
subscription_renewed_count_max = subscription_renewed_count.loc[subscription_renewed_count["renewed_count"].idxmax()]
print(subscription_renewed_count_max)


# Ploting a bar graph
import matplotlib.pyplot as plt # For interactive visulizations

plot_values = plt.bar(subscription_renewed_count["industry"],subscription_renewed_count["renewed_count"],color = "red")
plt.title("Renewal Clients by industries")
plt.xlabel("Industries")
plt.ylabel("Number of Renewal Clients")
plt.tight_layout()
plt.show()
