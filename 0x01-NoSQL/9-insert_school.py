"""9-insert_school.py"""
def insert_school(mongo_collection, **kwargs):
    """insert_school function"""
    doc = mongo_collection.insert_one(kwargs)
    return doc.inserted_id
