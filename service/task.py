# _*_ coding: utf-8 _*_
"""
@todo: 转码任务逻辑
"""

from lib.store import find, update, get_file_by_id, add_file, find_one, insert
from settings_run import CONTENT_TYPE_LIST
from settings_run import PLAY_LIST_TYPE
import os
from scn import new_scn
import subprocess 
from subprocess import Popen, PIPE, STDOUT
import re

def get_not_conver_file():
    """
    @todo: 取得所有没有转码的文件
    """
    file_queue  =  find("fs.files",{ "contentType": {"$in": CONTENT_TYPE_LIST },'converdid': {'$exists': False}})
    print file_queue
    return file_queue 

def remove_tmp_file():
    """
    @todo:删除所有临时文件 
    """
    os.popen("rm -rf /tmp/tmp")
    os.popen("rm -rf /tmp/tmp.flv")
    
def convert_file_2_flv(_id):
    """
    @todo: 把视频音频转为FLV格式
    @param _id: 文件ID
    """
    file_obj = get_file_by_id(_id) 
    open("/tmp/tmp", "w").write(file_obj.get("content"))
    print "------------------king is king "
    os.system("ffmpeg -i /tmp/tmp -y -ab 56\
                  -ar 22050 -b 500 -qscale 1  -s  320*240 /tmp/tmp.flv"
              )
    stream = open("/tmp/tmp.flv").read()
    converd_id = add_file(stream, 
        content_type="video/x-flv",
        filename=str(_id) + ".flv") 
    remove_tmp_file()
    return str(converd_id)
    
def update_file_converd(source_id, converd_id):
    """
    @todo: 更新转码文件ID到源文件
    @param source_id:源文件id
    @param converd_id:转码文werhID
    """
    update (
        "fs.files",
        {
          "_id": source_id
        },
        {
          "converd": True,
          "converdid": converd_id
        }
        
    )
 
    update (
        "fs.files",
        {
          "_id": converd_id
        },
        {
          "uuid": converd_id
        }
        
    )

def convert_media():
    """
    @todo: 转码所有未转码的文件
    """
    qeue = get_not_conver_file()  
    print "the quee is "
    print qeue
    for item in qeue:
        source_id = item.get("_id")
        update_file_converd(source_id, 
            convert_file_2_flv(source_id)
        )
    return True

def has_media_field(field):
    """
    @todo: 判断单个任务控件没有多媒体数据
    @param field: 任务控件数据 
    """
    if field.get("fieldType", "") in PLAY_LIST_TYPE:
        return True
    else:
        return False

def has_media(entry_list):
    """
    @todo: 判断单个任务数据有无多媒体数据
    @param entry_list: 任务数据
    """
    for field in entry_list:
        if has_media_field(field):
            return True
    return False   

def is_converd(entry_list):
    """
    @todo: 判断单个任务数据多媒体数据是否被转码
    @param entry_list: 任务数据
    """
    if not has_media(entry_list):
        return False
    for field in entry_list:
        if has_media_field(field):
            if not find_one("fs.files", {
                "uuid": field.get("uuid"),
                "converd": True
                }):
                return False 
    return True

def get_converd_id(uuid):
    """
    @todo: 通过UUID获取文件
    @param uuid: uuid
    """
    return find_one("fs.files", {"uuid": uuid}).get("converdid")

def get_converd(entry_list):
    """
    @todo: 追加转码文件ID到任务数据
    @param entry_list: 控件数据信息
    """
    converd_list = []
    for field in entry_list:
        if field.get("fieldType", "") in PLAY_LIST_TYPE:
            field["converdid"] = get_converd_id(field.get("uuid")) 
            converd_list.append(field)
        else:
            converd_list.append(field)

    return converd_list

def update_one_task_data(data):
    """
    @todo: 更新转码信息到任务数据
    @param data:任务数据信息
    """
    entry_list = data.get("entryList", [])
    if is_converd(entry_list):
        update("TaskData", {
           "_id": data.get("_id"),
           },
           {
             "converd": True,
             "entryList": get_converd(entry_list) 
           }
        )
     
def update_task_data_media():
    """
    @todo: 更新所有转码信息到任务数据 
    """
    qeue = find("TaskData", {
        "converd": False
    })
    for data in qeue:
        update_one_task_data(data) 
          
def insert_scn(new_scn, company):
    new_scn["corpSeq"] = company.corp_seq
    new_scn["checkedScenario"] = False
    if new_scn.has_key("_id"):
        new_scn.pop("_id")
    insert("Scenario", new_scn)



  
