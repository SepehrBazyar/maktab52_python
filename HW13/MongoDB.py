# Written by: Sepehr Bazyar
import pymongo
import logging

from company_data import *
from pprint import pprint

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)-10s - %(message)s')

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.company
logging.info("Connecting to Company DataBase...")

if not db.list_collection_names():
    for item in product_list:
        db.products.insert_one(item)

    for item in markup_list:
        db.markups.insert_one(item)
    
    for item in commission_list:
        db.commissions.insert_one(item)
    
    for item in user_list:
        db.users.insert_one(item)

    logging.info("Documents Writted into the Collections.")

products = db.products
markups = db.markups
commissions = db.commissions
users = db.users

