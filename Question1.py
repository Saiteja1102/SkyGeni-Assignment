# How many finance lending and blockchain clients does the organization have?

import pandas # For data Analysis

industry_client_details_table = pandas.read_csv("industry_client_details.csv")
# Here we are using pandas library to read the csv file i.e to import the file
print(industry_client_details_table)
# Just checking wheather the corect file has been imported or not and also verifying the data

clients = industry_client_details_table[industry_client_details_table["industry"].isin(["Finance Lending","Block Chain"])]
# From the table, we know that industry column has different values
# We need check for the Finanace and Blockchain
# We check whether these values are present in industry column or not
number_clients = clients["client_id"].count()
# Count the Total number of client_id
print(number_clients) # Answer is dispalyed


# Bar chart
import matplotlib.pyplot as plt # For interactive visulizations

industry_client_details_count = industry_client_details_table["industry"].value_counts()
# Finds the total number of clients in each industry
plot_values = industry_client_details_count.plot(kind="bar",color="green") # Plot the bar graph
plt.title("Number of Clients by Industry") # Title of the graph
plt.xlabel("Industry") # X-Axis Name
plt.ylabel("Number of Clients") # Y-Axis Name
plt.tight_layout() # Adjust layout to prevent label cutoff
plt.bar_label(plot_values.containers[0]) # Display values on top it
plt.show() # Display the graph (similar to print)