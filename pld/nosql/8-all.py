#!/usr/bin/env python
"""
, ObjectId
from typing import List, Dict


def insert_school(mongo_collection: collection, **kwargs) -> ObjectId:
    """"""
    get_ins_id =mongo_collection.insert_one(kwargs) 
    return 

"""
from pymongo import collection, MongoClient

table = {k: str(v) for k,v in vars().items()}
message= ' '.join([f'{k}: ' + '{' + k + '};' for k in table.keys()])
print(message.format(**table))
