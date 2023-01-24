import os
import pymongo
import json

from dotenv import load_dotenv
load_dotenv('mongodb-import/.env')

MONGO_DB_PASSWORD = os.environ.get("MONGO_DB_PASSWORD")
MONGO_DB_DATABASE = os.environ.get("MONGO_DB_DATABASE").replace(
    "<password>", MONGO_DB_PASSWORD)

myclient = pymongo.MongoClient(MONGO_DB_DATABASE)
mydb = myclient["ecommerce"]
myproducts = mydb["products"]

f = open("mongodb-import/products.json")
myproducts_data = json.load(f)

x = myproducts.insert_many(myproducts_data)
