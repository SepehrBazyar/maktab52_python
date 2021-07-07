# Written by: Sepehr Bazyar
from pymongo import MongoClient
from company_data import *
from pprint import pprint

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)-10s - %(message)s')

def calculate_markup_percent(product_type: str, count: int) -> float:
    """
    Query to Calculate Markup of Product by Percent Unit\n
    Markup for 1 Count Lower Cost and Greater than Lower Count is Equal Upper Cost\n
    Other Count Liner. For Example: calculate_markup_percent("1", 5) = 14.44
    """

    query = {"product_type": product_type}
    res = markups.find_one(query, {"_id": 0, "lower_cost": 1, "upper_cost": 1, "lower_count": 1})
    m = (res["upper_cost"] - res["lower_cost"]) / (res["lower_count"] - 1)
    h = res["upper_cost"] - (m * res["lower_count"])
    return float(round(m * count + h, 2))

def calculate_product_price():
    pass

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

name  = input("Please Enter Your Name: ").split()
query = {"first_name": name[0], "last_name": name[1]}
userid = users.find_one(query, {"userid": 1, "_id": 0})
