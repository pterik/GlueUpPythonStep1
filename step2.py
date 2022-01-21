from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint

def find_document(collection, elements, multiple=False):
    """ Function to retrieve single or multiple documents from a provided
    Collection using a dictionary containing a document's elements.
    """
    if multiple:
        results = collection.find(elements)
        return [r for r in results]
    else:
        return collection.find_one(elements)

# main app

client = MongoClient("mongodb://localhost:27017")
db = client['kpmg_mongo']
#series_collection = db['contact_history']
#result = find_document(series_collection, {})
#print("result={}".format(result))
collections = db.list_collection_names()
for collection in collections:
    print("collection_name={}".format(collection))
    print(db[collection])
    obj=db[collection]
    #collection.find({})
    print(obj)
#    table=db.collection
#    first_instance=table.find_one()
#    print("First_instance={}".format(first_instance))
