import os
import pymongo
import json
import bson
import datetime

from dotenv import load_dotenv
load_dotenv('mongodb-import/.env')


def Average(lst):
    return sum(lst) / len(lst)


MONGO_DB_PASSWORD = os.environ.get('MONGO_DB_PASSWORD')
MONGO_DB_DATABASE = os.environ.get('MONGO_DB_DATABASE').replace(
    '<password>', MONGO_DB_PASSWORD)

myclient = pymongo.MongoClient(MONGO_DB_DATABASE)
mydb = myclient['ecommerce']

myproducts = mydb['products']
myreviews = mydb['reviews']
myusers = mydb['users']

myproducts_data = json.load(open('mongodb-import/products.json'))
myreviews_data = json.load(open('mongodb-import/reviews.json'))
myusers_data = json.load(open('mongodb-import/users.json'))

for myproduct in myproducts_data:
    ratings = []

    for myreview in myreviews_data:
        if myreview['product'] == myproduct['_id']:
            ratings.append(myreview['rating'])

    i = myproducts_data.index(myproduct);
    
    myproducts_data[i] = {
        '_id': bson.ObjectId(myproduct['_id']),
        'name': myproduct['name'],
        'price': myproduct['price'],
        'priceCompare': myproduct['priceCompare'],
        'avgRatings': Average(ratings),
        'numReviews': len(ratings),
        'imgs': myproduct['imgs'],
        'description': myproduct['description'],
        'createdAt': datetime.datetime.now()
    }
    
x = myproducts.insert_many(myproducts_data)
y = myreviews.insert_many(myreviews_data)
z = myusers.insert_many(myusers_data)

print('Successfully imported!');