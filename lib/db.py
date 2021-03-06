import settings_run as settings
import pymongo
import gridfs
MG_HOST = settings.MONGO_HOST
MG_PORT = settings.MONGO_PORT
MG_READ_HOST = settings.MONGO_HOST
MG_READ_PORT = settings.MONGO_PORT
MG_NAME = settings.DB_NAME

def get_db_update():
    _db = pymongo.Connection(MG_HOST, MG_PORT)
    _db = _db[MG_NAME]
    _db.authenticate("xia","c2vm.c0m")
    return _db


def get_db_read():
    _db = pymongo.Connection(MG_HOST, MG_PORT)
    _db = _db[MG_NAME]
    _db.authenticate("xia","c2vm.c0m")
    return _db
db_update = get_db_update()
db = get_db_read()


def get_gridfs():
    return gridfs.GridFS(db_update)
    


