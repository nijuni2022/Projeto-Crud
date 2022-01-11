#from bson.objectid import ObjectId
from pymongo import MongoClient



client= MongoClient("localhost", 27017)

db = client.Dados