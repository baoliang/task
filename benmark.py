# _*_ coding: utf-8 _*_
from lib.store import insert, update, find, find_one, remove, add_file
import unittest
import random
from lib.utils import now

def insert_data():
    for i in range(100000):
          user = [ {
              "userSeq": u,
              "userId": "test",
              "userName": "test"
          } for u in range(random.randint(1, 1000))] 
          insert("TaskPlan",{
              "className" : "com.c2vm.xia.rest.taskplan.bean.TaskPlan",
              "taskSeq" : "4f90d10e0364dcca1c7ad26d",
              "taskName" : "1",
              "projSeq" : 43,
              "projName" : "1",
              "projIcon" : "",
              "userId" : "",
              "multiTask" : "T",
              "taskSchedule" : "",
              "markLoct" : "1",
              "indexTag" : "",
              "description" : "",
              "corpSeq" : 17,
              "crtDate" : "2012-04-20T02:59:26.996Z",
              "crtUser" : 65,
              "uptDate" : "2012-04-20T03:56:24.791Z",
              "uptUser" : 65,
              "uptStat" : "E",
              "version" : 1,
              "taskStatus" : "N",
              "taskIconUrl" : "",
              "userList" : user,
              "entryList" : [
                  {
                      "className" : "com.c2vm.xia.viewcomponent.Camera",
                      "fieldType" : "Camera",
                      "comLabel" : "fasd",
                      "dataLabel" : "fasd",
                      "direction" : "up",
                      "url" : "/rest/service/resource/company/17/project/43/upload",
                      "size" : "854*480",
                      "layout" : "RL/UD",
                      "required" : False
                  },
                  {
                      "className" : "com.c2vm.xia.viewcomponent.Location",
                      "fieldType" : "Location",
                      "comLabel" : "dsa",
                      "name" : "111 ",
                      "latitude" : "",
                      "longitude" : "",
                      "layout" : "RL/UD",
                      "required" : False
                  }
              ]
        })
         
def test_task_user_find():
    print "start"
    print now()
    result = find("test_task", {"userList.userSeq": 5}, return_type="cusor")
    print now()
    #查询没问题  
    result = find("test_task", {"userList.userSeq": 5})
    #取数据很慢非常慢
    print "end"
    print result
    print result.count()

