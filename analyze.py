# Sales Analysis
# A simple script that reads sales data and prints a short summary.
# All data is dummy content, used for practicing Git & GitHub.

import pandas as pd

# Load the data from the CSV file.
data = pd.read_csv("data.csv")

# Show the first few rows so we can see what the data looks like.
print("First rows of the data:")
print(data.head())
print()

# Total revenue across everything.
total_revenue = data["revenue"].sum()
print("Total revenue:", total_revenue)

# Total number of orders.
total_orders = data["orders"].sum()
print("Total orders:", total_orders)
print()

# Revenue for each region.
print("Revenue by region:")
revenue_by_region = data.groupby("region")["revenue"].sum()
print(revenue_by_region)
print()

# The region with the highest revenue.
best_region = revenue_by_region.idxmax()
print("Best region:", best_region)
