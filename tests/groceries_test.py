from app.groceries import calculate_average_price
from pandas import read_csv
import os

test_sample_1 = [{'name':'tacos','price':'1'},{'name':'fish','price':'1'},{'name':'chips','price':'10'}]
test_sample_2 = read_csv(os.path.join(os.path.dirname(__file__), "..", "data", "default_products.csv"))

def test_calculate_average_price():
    assert calculate_average_price(test_sample_1) == 4.0
    assert calculate_average_price(test_sample_2) == 8.37

