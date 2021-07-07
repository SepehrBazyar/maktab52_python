# Written by: Sepehr Bazyar
from pymongo import MongoClient
from company_data import *

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)-10s - %(message)s')

def calculate_markup_percent(product_type: str, count: int) -> float:
    """
    Query to Calculate Markup of Product by Percent Unit.\n
    Markup for 1 Count Lower Cost and Greater than Lower Count is Equal Upper Cost.\n
    Other Count Calculate Liner. For Example: calculate_markup_percent("1", 5) = 14.44
    """

    query = {"product_type": product_type}
    res = markups.find_one(query, {"_id": 0, "lower_cost": 1, "upper_cost": 1, "lower_count": 1})
    m = (res["upper_cost"] - res["lower_cost"]) / (res["lower_count"] - 1)
    h = res["upper_cost"] - (m * res["lower_count"])
    return float(round(m * count + h, 2)) if count < res["lower_count"] else float(res["upper_cost"])

def calculate_product_price(product_type: str, count: int, userid: int = None) -> float:
    """
    Query to Calculate Price of Product by Commission User in Dollar Unit.\n
    It is Possible to Buy for Everyone so userid Parametr is Optional.
    """

    query = {"type": product_type}
    prod = products.find_one(query, {"_id": 0, "price": 1, "commission_groups": 1})
    ans = prod["price"] * (1 - calculate_markup_percent(product_type, count) / 100)

    if userid:
        for commission in prod["commission_groups"]:
            query = {"group_name": commission}
            res = commissions.find_one(query)
            if userid in res["users"]:
                if res["unit"] == "percent":
                    ans *= (1 - res["cost"] / 100)
                else:
                    ans -= res["cost"]
    return ans

client = MongoClient('mongodb://localhost:27017/')
db = client.company
logging.info("Connecting to Company DataBase...")

if not db.list_collection_names(): #create collections in database
    db.products.insert_many(product_list)
    db.markups.insert_many(markup_list)
    db.commissions.insert_many(commission_list)
    db.users.insert_many(user_list)
    logging.info("Documents Writted into the Collections.")

products = db.products
markups = db.markups
commissions = db.commissions
users = db.users

name   = input("Please Enter Your Name: ").split()
query  = {"first_name": name[0], "last_name": name[1]}
userid = users.find_one(query, {"userid": 1, "_id": 0})

orders = input("""Please Enter Your Orders:
(For Example -> ProductName1 Count1 ProductName2 Count2 ...)
>>> """).split()

price = 0
for counter in range(0, len(orders), 2):
    query = {"name": orders[counter]}
    res = products.find_one(query, {"_id": 0, "type": 1})
    if res:
        if userid:
            price += calculate_product_price(res["type"], int(orders[counter + 1]), userid)
        else:
            price += calculate_product_price(res["type"], int(orders[counter + 1]))
    else:
        logging.error(f"{orders[counter]} is not in the Product List.")
print(f"\nTotal Price of Your Recepites is Equal {price:.2f}$.")
