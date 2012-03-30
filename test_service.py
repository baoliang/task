# _*_ coding: utf-8 _*_
from lib.store import insert, find, find_one, remove
from service.task import get_not_conver_file
from service.task import convert_task
import unittest

class Test_account(unittest.TestCase):    
    def setUp(self):
        pass	 
    def tearDown(self):
        pass		 
    def test_get_not_conver_file(self):
        self.assertTrue(len(get_not_conver_file()) > 0) 
    
    def test_convert_task(self):
        result = convert_task()
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
