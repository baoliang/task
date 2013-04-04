from lib.db import db_update, db, get_gridfs

import pymongo
from bson.objectid import ObjectId
import datetime
import settings_run

def update(collection, query, data_dic):
    if query.has_key("_id"):
        query["_id"] = ObjectId(str(query["_id"]))
    db_update[collection].update(query, {'$set': data_dic} )
   
def insert(collection, data, st_code=settings_run.ST_CODE['norm']):
    data.update({'create_time': str(datetime.datetime.now())})
    data.update({'st_code': st_code})
    return db_update[collection].insert(data)
    
def remove(collection, query={}, real=False):
    if real:
        db_update[collection].remove(query)
    else:
        db_update[collection].update(
            query, 
            {
                '$set':
                {
                    'st_code': settings_run.ST_CODE['del']
                }
            }
        )


def find(collection, query={}, limit=0, sort=-1, return_type="list"):
    #query.update({'st_code': settings_run.ST_CODE['norm']})
    result = db[collection].find(query).sort('create_time', sort).limit(limit)
    if return_type == "cusor":
        return result
    else:
        return list(result)

def find_one(collection, query={}):
    if query.has_key('_id')  and collection not in ['users', 'city', 'cach']:
        query.update({'_id': ObjectId(query.get('_id'))})
    return db[collection].find_one(query)
    
def add_file(file, content_type, filename):
    fs = get_gridfs()
    res = fs.put(
        file,
        content_type=content_type,
        filename=filename
    )
    return  res

def get_file_by_id(_id):
    fs = get_gridfs()
    file = fs.get(ObjectId(_id))
    
    return  {"content":file.read()}
   
