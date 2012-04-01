# _*_ coding: utf-8 _*_
from lib.store import insert, find, find_one, remove, add_file
from service.task import get_not_conver_file
from service.task import convert_task
from service.task import remove_tmp_file
import unittest
import os

class Test_account(unittest.TestCase):    
    _id = ""
    def setUp(self):
        remove_tmp_file() 
        self._id = str(add_file(open("./tmp.mov").read(), 
            content_type="video/quicktime",
            filename="tmp.mov"
        ))
    def tearDown(self):
        remove("fs.file", self._id, real=True)		 

    def test_get_not_conver_file(self):
        self.assertTrue(get_not_conver_file() > 0) 
    
    def test_convert_task(self):
        result = convert_task()
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
