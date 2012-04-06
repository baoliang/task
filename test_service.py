# _*_ coding: utf-8 _*_
from lib.store import insert, update, find, find_one, remove, add_file
from service.task import get_not_conver_file
from service.task import convert_media
from service.task import remove_tmp_file
from service.task import update_task_data_media
import unittest
import os

class Test_account(unittest.TestCase):    
    _id = ""
    task_id = ""
    file_id =""
    def setUp(self):
        remove_tmp_file() 
        self._id = str(add_file(open("./tmp.mov").read(), 
            content_type="video/quicktime",
            filename="tmp.mov", 
            
        ))
        
        update("fs.files",{"_id": self._id}, {"uuid": self._id})
        self.task_id = insert("TaskData", {
          "entryList":[{
            "fieldType":"Video", "uuid": self._id
              }]
          })
       

    def tearDown(self):
        remove("fs.file", {"_id": self._id}, real=True)
        remove('TaskData', {"_id": self.task_id}, real=True)
    def test_get_not_conver_file(self):
        self.assertTrue(get_not_conver_file() > 0) 
    

    def test_convert_media(self):
        result = convert_media()
        self.assertTrue(result)
        update_task_data_media()
        result = find_one("TaskData", {
            "_id": self.task_id
         } )
        print "result"
        print result
        self.assertTrue(result.get("converd", False))
        self.assertTrue(result.get("entryList")[0].get("converdid", False))
            
if __name__ == '__main__':
    unittest.main()
