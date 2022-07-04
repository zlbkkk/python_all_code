# 此py文件主要是获取cookie和写cookie到文件

import os
import sys
import json

from Util.handle_json import read_json,wrire_value

base_path = os.path.dirname(os.getcwd())
sys.path.append(base_path)

# 要封装的函数：
# 1、获取cookies
# 2、写入cookies

'''
    将cookie写入到文件中的函数，思路如下：
        def get_cookie_value():
        
            1、作用：把cookie.json文件的内容全部拿到，为后面在某个键值下写入cookie做准备写入
            比如写到cookie.json文件中键值为app的键下
            read_json()就是获取json文件数据的，直接调用即可
        
            2、注意：将cookie写入到json文件时，要把它写入到某个键下，如果是覆盖写的话，
            那之前存的cookie就会丢失，
        
    
            
            data1={
                "aaa":"jjkj"
            }
        
            #目前这个data是获取到了cookie.json的全部内容，到时候更新完某个键的cookie之后，在全部写入
            
            data = read_json("/Config/cookie.json") # read_json()函数已经有basepath了，只需要传文件路径就行
            
            data["web"]=data1 # 更新某个键值的cookie
            wrire_value(data) # 再全部写入

'''



def get_cookie_value(cookie_key):

    '''
    作用：根据键值获取cookie.json文件中的cookie值，这个函数字run_main（）中使用：

    if cookie_metnod=="yes":
         cookie=get_cookie_value("app")

    '''
    data = read_json("/Config/cookie.json") # read_json()函数已经有basepath了，只需要传文件路径就行
    return data[cookie_key] # 传入cookie的key，明确获取哪个cookie



def write_cookie(data,cookie_key):

    # 注意：这个形参data就是实际的cookie，在以后调用函数时传入

    data1 = read_json("/Config/cookie.json") # 获取cookie.json文件的全部内容
    data1[cookie_key] = data # 更新cookie文件中某个键的值
    wrire_value(data1) # 上面已经更新了，现在在全部内容再次写入cookie.json文件中




# if __name__=="__main__":
#     print(get_cookie_value("app1"))
#     data={
#         "cookie1":"zlb"
#     }
#
#     write_cookie(data,"app1")







