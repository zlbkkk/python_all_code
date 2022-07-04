#coding=utf-8


import requests
import unittest
from unittest import mock



class Count():

    def add(self):
        pass



# test Count class
class TestCount(unittest.TestCase):

    def test_add(self):
        count = Count()
        Count.add = mock.Mock(return_value=13) #这个是对add函数的mock的结果

        result = count.add(8,9) # 这个是实际调用的结果
        self.assertEqual(result,13)


if __name__ == '__main__':
    unittest.main()


