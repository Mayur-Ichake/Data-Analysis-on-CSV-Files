# Data Analysis on CSV Files
"""Hints/Mini Guide:
1.Load CSV using Pandas
2.Use groupby(), sum(), plot()"""

# import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
data = pd.read_csv("sales_data_sample.csv", encoding='latin1')
print("Data loaded successfully!")

print("Basic Information:")
print(data.info())

# groupby() and mean()
result = data.groupby("PRODUCTLINE")["SALES"].mean()
print("\nAverage Sales by Product Line:\n", result)

# sum()
sales_by_product = data.groupby("PRODUCTLINE")["SALES"].sum()
print("\nTotal Sales by Product Line:\n", sales_by_product)

sales_by_country = data.groupby("COUNTRY")["SALES"].sum()
print("\nTotal Sales by Country:\n", sales_by_country)

# using plot()
# Bar plot for sales by product line
sales_by_product.plot(kind="bar", title="Sales by Product Line")
plt.xlabel("Product Line")
plt.ylabel("Total Sales")
plt.show()

# Pie chart for sales by country
sales_by_country.plot(kind="pie", autopct="%1.1f%%", title="Sales by Country")
plt.ylabel("")  
plt.show()
