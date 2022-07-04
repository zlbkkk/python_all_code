import requests
import json

from Util.handle_ini import HandleInit
from Util.handle_json import get_value
from Util.handle_cookie import write_cookie

handle_ini = HandleInit() # 实例化操作ini的类


class BaseRequest:

    def send_post(self,url,data,cookie=None,get_cookie=None,header=None):

        respone = requests.post(url=url,data=data,cookies=cookie,headers=header)

        if get_cookie != None:
            '''
                get_cookie={"is_cookie":"app"}
            '''
            cookie_value_jar = respone.cookies # 获取cookie,是一个cookiejar对象，需要下一行进行如下转换,参考：https://blog.csdn.net/qq_43546676/article/details/102942975

            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)

            write_cookie(cookie_value,get_cookie["is_cookie"]) # 写cookie放到这里来写，cookie_value就是cookie

        res = respone.text #用.text，不能使用.json()，因为有可能接口返回的不是json格式就会报错

        return res

    def send_get(self,url,data,cookie=None,get_cookie=None,header=None):

        respone = requests.get(url=url, params=data, cookies=cookie,headers=header)

        if get_cookie != None:

            '''
              get_cookie={"is_cookie":"app"}
            '''

            cookie_value_jar = respone.cookies  # 获取cookie,是一个cookiejar对象，需要下一行进行如下转换,参考：https://blog.csdn.net/qq_43546676/article/details/102942975

            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)

            write_cookie(cookie_value, get_cookie["is_cookie"])  # 写cookie放到这里来写，cookie_value就是cookie

        res = respone.text  # 用.text，不能使用.json()，因为有可能接口返回的不是json格式就会报错

        return res # res一定要返回出去，因为在run_main.py中的run_case()函数中，后面是要拿响应报文来做断言的

    def run_main(self,method,url,data,cookie=None,get_cookie=None,header=None):

        # return get_value(url)

        base_url = handle_ini.get_value("host") # 获取ini中的host的值
        # print(base_url)
        '''
            解释1：
                因为excel中url单元格的值是api3/beta4这个样式的，不是全部的路径，但也有可能是全部的路径，
                全部的路径那就是包含http，所以现在做判断，如果是全路径，那url就直接等于excel中url单元格的值；
                如果不是全路径，那就拿ini文件中的url和传进来的url相加拼接，组成一个完整的url，
                注意：ini文件中会维护一个根域名，通常在excel中会只写路径，比如：/login

        '''

        if "http" not in url: # 参考：解释1
            url = base_url+url

        # print(url)

        if method == "post":
            res = self.send_post(url,data,cookie,get_cookie,header)
        else:
            res = self.send_get(url,data,cookie,get_cookie,header)

        try:
            res = json.loads(res)

        except:
            print("这是一个text")

        return res


# request = BaseRequest()


# if __name__=="__main__":
#     request = BaseRequest()
#
#     t=request.run_main("post","login","{'username':'1111'}")
#     print(t)


