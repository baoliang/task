from service.task import convert_media 
from celery.decorators import task
from service.task import update_task_data_media
from service.task import ex_java
from lib.utils import now

import os

@task    
def convert_task():
    convert_media()

@task
def update_task(): 
    update_task_data_media() 
    
    
@task
def test_java_task():
    result = ex_java(['java', "-jar sync-task-data/sync-task-data.jar"])
    if  not result[0]:
        raise NameError(result[1])
    else:
        return result[1]
        
@task
def insert_data_from_mongo():
    import os
    os.system("java FileStreamDemo")

@task    
def monit_mongodb():
    try:
        from lib.db import db
    except:
        os.system("sudo su")
        os.system("cp /home/xia/mongo.log "+now()+"mongo.log")
        os.system("rm -rf /opt/mongodb/data/mongod.lock")
        os.system("/opt/mongodb/bin/mongod --port 32508 --dbpath /opt/mongodb/data/ --fork --logpath /home/xia/mongo.log")