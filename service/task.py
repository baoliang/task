from lib.store import find, update, get_file_by_id
from settings_run import CONTENT_TYPE_LIST
import os
from lib.utils import print_err
def get_not_conver_file():
    file_queue = find("fs.files",
        {
          "$and": [{ "contentType": {
              "$in": CONTENT_TYPE_LIST  
              }},
              {'converd': {'$exists': False}}]
         }
      )
    return file_queue 

def convert_file_2_flv(_id):
    file = get_file_by_id(_id) 
    open("/tmp/tmp", "w").write(file.get("content"))
    result  = os.popen("ffmpeg -i /tmp/tmp -y -ab 56 -ar 22050 -b 500 -r 15 -s 320*240 /tmp/tmp.flv")
    stream = open("/tmp/tmp.flv").read()
    converd_id = add_file(stream, 
        "video/x-flv", _id + ".flv") 
    os.open("rm -rf /tmp/tmp")
    os.open("rm -rf /tmp/tmp.flv"
    return converd_id
        
def update_file_converd(source_id, converd_id):
    update (
        "fs.files",
        {
          "_id": source_id
        },
        {
            "$set": {
                "converd": True,
                "converd_id": converd_id
            }
        }
    )
   
def convert_task():
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
