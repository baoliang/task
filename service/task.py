from lib.store import find, update, get_file_by_id, add_file, find_one
from settings_run import CONTENT_TYPE_LIST
from settings_run import PLAY_LIST_TYPE
import os
from lib.utils import print_err
import time
def get_not_conver_file():
    file_queue = find("fs.files",
        {
          "$and": [{ "contentType": {
              "$in": CONTENT_TYPE_LIST  
              }},
              {'converd_id': {'$exists': False}}]
         }
      )
    return file_queue 

def remove_tmp_file():
    os.popen("rm -rf /tmp/tmp")
    os.popen("rm -rf /tmp/tmp.flv")
    
def convert_file_2_flv(_id):
    file = get_file_by_id(_id) 
    open("/tmp/tmp", "w").write(file.get("content"))
    result  = os.system("ffmpeg -i /tmp/tmp -y -ab 56 -ar 22050 -b 500 -s 320*240 /tmp/tmp.flv")
    stream = open("/tmp/tmp.flv").read()
    converd_id = add_file(stream, 
        content_type="video/x-flv",
        filename=str(_id) + ".flv") 
    remove_tmp_file()
    return str(converd_id)
    
def update_file_converd(source_id, converd_id):
    update (
        "fs.files",
        {
          "_id": source_id
        },
        {
          "converd": True,
          "converd_id": converd_id
        }
        
    )
 
def convert_media():
    try:
        qeue = get_not_conver_file()  
        for item in qeue:
            source_id = item.get("_id")
            update_file_converd(source_id, 
                convert_file_2_flv(source_id)
            )
        return True
    except:
        print_err()
        return False

def has_media_field(field):
    if field.get("fieldType", "") in PLAY_LIST_TYPE:
        return True
    else:
        return False

def has_media(entryList):
    
    for field in entryList:
        if has_media_field(field):
            return True
    return False   

def is_converd(entryList):
    if not has_media(entryList):
        return False
    for field in entryList:
        if has_media_field(field):
            if not find_one("fs.files", {
                "uuid": field.get("uuid"),
                "converd": True
                }):
                return False 
    return True

def get_converd_id(uuid):
    return find_one("fs.files", {"uuid": uuid}).get("converd_id")

def get_converd(entryList):
    converd_list = []
    for field in entryList:
        if field.get("fieldType", "") in PLAY_LIST_TYPE:
            field["converd_id"] = get_converd_id(field.get("uuid")) 
            converd_list.append(field)
        else:
            converd_list.append(field)

    return converd_list

def update_one_task_data(data):
    entryList = data.get("entryList", [])
    if is_converd(entryList):
       print 'converd_id'
       print data.get("_id")
       update("TaskData", {
           "_id": data.get("_id"),
           },
           {
             "converd": True,
             "entryList": get_converd(entryList) 
           }
       )
     
def update_task_data_media():
    try:
        qeue = find("TaskData", {
            "converd": {"$exists": False}
        })
        for data in qeue:
            print "update_task"
            print data.get("_id")
            update_one_task_data(data) 
    except:
        print_err()
        return False
                    
