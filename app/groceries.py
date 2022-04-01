
from typing import Dict
from numpy import product
from app.utils import to_usd

# READ INVENTORY OF PRODUCTS
import os

# base filepath to where the codebase cleanup file is, then go to data file within:
base_filepath = os.path.join(os.path.dirname(__file__), "..", "data")

# modifies the base filepath for the custom and default files:
products_filepath = os.path.join(base_filepath, "products.csv")
default_filepath = os.path.join(base_filepath, "default_products.csv")

# checks to see if a products.csv file exists. If not, it uses the default
if products_filepath == True:
    print("USING CUSTOM PRODUCTS CSV FILE...")
    csv_filepath = products_filepath
else:
    print("USING DEFAULT PRODUCTS CSV FILE...")
    csv_filepath = default_filepath



from pandas import read_csv

#reads the csv file into products variable
products = read_csv(csv_filepath)

#pandas transforms the data into a list of dictionaries
products = products.to_dict('records')



# PRINTED INVENTORY REPORT

print("---------")
print("THERE ARE", len(products), "PRODUCTS:")
print("---------")

all_prices = []
for p in products:
    print("..." + p["name"] + "   " + to_usd(p["price"]))
    all_prices.append(float(p["price"]))

def calculate_average_price(products):

    all_prices = []
    for p in products:
        all_prices.append(float(p["price"]))
    from statistics import mean
    from app.utils import to_usd
    avg_price = mean(all_prices)
    print("---------")
    print("AVERAGE PRICE:", to_usd(avg_price))
    print("---------")

calculate_average_price(products)





# EMAIL INVENTORY REPORT
