# Data Analysis on CSV Files
"""Hints/Mini Guide:
1.Load CSV using Pandas
2.Use groupby(), sum(), plot()"""

"""Steps : """

import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("sales_data_sample.csv", encoding='latin1')
print("Data loaded successfully!\n")

print("Basic Information:")
print(data.info())

sales_by_product = data.groupby("PRODUCTLINE")["SALES"].sum()
print("\nTotal Sales by Product Line:\n", sales_by_product)

sales_by_country = data.groupby("COUNTRY")["SALES"].sum()
print("\nTotal Sales by Country:\n", sales_by_country)


sales_by_product.plot(kind="bar", title="Sales by Product Line")
plt.xlabel("Product Line")
plt.ylabel("Total Sales")

sales_by_country.plot(kind="pie", autopct="%1.1f%%", title="Sales by Country")
plt.ylabel("")  
plt.show()
