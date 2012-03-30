#coding= utf-8
from store import find
from datetime import datetime
from lib.utils import now
import settings_run
import time
from lib.db import db
def get_page(
    collection,
    query={},
    limit=settings_run.DEFAULT_LIMIT
    ):
    '''
    @todo:获取分页
    @params collection:集合名称
    @params query:查询
    @params page: 页数
    @params limit: 数据数量
    @return:
    '''      

    page = int(query.get('page', 1))  
    boot_time = query.get('boot_time', None)
    if not boot_time or page == 1:
        boot_time = now()
    query['create_time'] = {
               '$lt': str(boot_time)
                
            }
 
    if query.has_key('page'): query.pop('page')
    if query.has_key('old_page'): query.pop('old_page')
    if query.has_key('boot_time'): query.pop('boot_time')
   
    collection_data = find(collection, query, limit=limit)
    
    data = list(collection_data)
    length = len(data)
    if length > 0:
        boot_time = data[length-1].get('create_time')
    else:
        boot_time = ''
    if query.has_key('create_time'): query.pop('create_time')
    return {
        'count': find(collection, query, return_type="cusor").count(),
        'data': data,
        'page': page,   
        'limit': limit,
        'boot_time': boot_time,
    }
    
    
