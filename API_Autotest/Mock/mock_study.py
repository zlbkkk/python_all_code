#coding=utf-8
import mock
import requests
import unittest

from Util.handle_json import get_value


url = "http://www.imooc.com/login"
data = {
    "username":"111111",
    "password":"11112"
}




def get_request(url,data):
    #requests.post()
    #url = "http://www.imooc.com/login/register?user=111&pass=222"
    #url+data
    res = requests.get(url,params=data).json()
    return res

# print(post_request('http://127.0.0.1:8889/login',data=data))



def post_request(url,data):
    res = requests.post(url,data=data).json()
    return res

class TestLogin(unittest.TestCase):
    def setUp(self):
        print("case开始执行")


    def tearDown(self):
        print("case执行结束")
    
    def test_01(self):
        url = "http://www.imooc.com/login/register"
        data1_real = get_value("register")
        data_mock = {"username":"111111000"}

        # 定义mock的返回值，也就是需要mock返回data_mock值
        sucess_test = mock.Mock(return_value=data_mock)
        print(sucess_test)

    # 赋值给post_request函数对象,当这样写时：post_request()就是调用了上面的post_request函数
        post_request = sucess_test
        print("============")
        print(post_request())
        # res = post_request
        self.assertEqual(data1_real,post_request(),msg="不相等")  # res()实际上是执行了post_request()


    
if __name__=="__main__":
    unittest.main()