import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['csci2963_mongodb_lab']
collection = db.definitions

# fetch all the records
collection.find()
# fetch one record
collection.find_one()
# fetch a specific record
collection.find_one({"word": "Capitaland"})
# fetch a record by object id
collection.find_one({"_id": "56fe9e22bad6b23cde07b8ce"})
# insert a new record
collection.insert({"definition":" v. complicate, muddle, make unclear", "word":"Obfuscate"})
