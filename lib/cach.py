from lib.store import find_one, update, insert
def get_cach(key):
        return find_one('cach', {'_id': key})
def set_cach(key, data):
    if find_one('cach', {'_id': key}):
        update('cach', {'_id': key}, data)
    else:
        data['_id'] =  key
        insert('cach', data)
        