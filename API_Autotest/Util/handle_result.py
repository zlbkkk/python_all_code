import os
import sys
import json
from deepdiff import DeepDiff #比較兩個json文件的不同的庫

from Util.handle_json import get_value

base_path = os.path.dirname(os.getcwd())

# print(base_path)

# print(get_value("api3/getbanneradvertver2","/Config/code_message.json"))

def handle_result(url,code):
    '''
        从user_data.json文件中根据code获取事先写好的错误信息描述

        怎么使用？
        和接口返回的信息描述
        做对比，以此判断接口是否成功,user_data.json存放的是错误码和错误描述的字典

    '''
    date = get_value(url, "/Config/code_message.json") # url就是json文件中的key值，如下面的 api3/getbanneradvertver2
    # print(date)

    '''
    code_message.json的某个内容：
        "api3/getbanneradvertver2":[
        {"1006":"token error"},
        {"1007":"用户名错误"},
        {"1008":"密码错误"}
            ]
    
    '''
    if date != None:

        # message = i.get(code) # 这样写的话，循环第一个是1006(看上面),不是1007，此时就会直接返回None
        # return message

        '''
            解释1：
            对 i.get(str(code)) 中的str(code)的解释：
                # 在run_main()中从接口返回结果取到的 code = res['errorCode'] 是int类型，
                但是在code_messagr.json中的code是str类型，所以要转换，要不然取不到
        '''

        for i in date:
            message = i.get(str(code))  # 参考解释1
            if message:
                return message  # 返回错误码对应的错误描述信息

    return None

# print(handle_result("api3/getbanneradvertver2","1007"))


def get_result_json(url,status):
    '''
        函数作用：从result.json中获取写好的正确的报文，通过status，
        也就是sucess或者error部分的内容，获取正确部分的报文或者错误部分的报文
        将获取到的sucess或者error部分的内容,传到下面的handle_result_json()函数中，与返回的报文进行字典的对比，然后断言

    '''

    date = get_value(url, "/Config/result.json")
    if date != None:

        # message = i.get(code) # 这样写的话，循环第一个是1006(看上面),不是1007，此时就会直接返回None
        # return message

        for i in date:
            '''
            对 i.get(str(code)) 中的str(code)的解释：
                # 在run_main()中从接口返回结果取到的 code = res['errorCode'] 是int类型，
                但是在code_messagr.json中的code是str类型，所以要转换，要不然取不到
            '''
            message = i.get(str(status))  #参考上面handle_result()的解释
            if message:
                return message  # 返回sueccess或error的报文

    return None




def handle_result_json(dict1,dict2):
    '''
        通过比较两个json的结构体，来判断用例是否执行成功,一个json来自接口实际的执行结果
        一个json来自写在文件中的的json，通常是这个接口的正确的响应报文

    '''
    '''
    
        #1、使用DeepDiff比较两个字典：dict1和dict2的比较逻辑：
        
        注意：传值的时候，dict1表示接口返回的报文，dict2表示写在json文件中的报文
        
        1、dict1比dict2少了一个字段，其他都一样，会出现： dictionary_item_added
        2、dict1和dict2字段数一样，但是有一个字段的键和值都不一样，会出现：dictionary_item_added
        3、dict1和dict2字段数一样,键都一样，顺序可不一样，但是有一个键对应的值不一样，不会出现：dictionary_item_added
        4、dict1比dict2字段多了一个字段，不会出现dictionary_item_added，但是会出现:dictionary_item_removed
        5、dict1和dict2字段数一样,但是有一个字段的键，他的值的类型不同，一个是list类型，一个是dict类型，不会出现：dictionary_item_removed
        
    '''

    if isinstance(dict1,dict) and isinstance(dict2,dict):
        cmp_dict = DeepDiff(dict1,dict2,ignore_order=True).to_dict()
        # print(cmp_dict)
        # 以下if是通过DeepDiff判断两个json是否相同，以此判断是否用例是否执行成功
        if cmp_dict.get("dictionary_item_added"): # 不能只判断包含有values_changed，因为有可能是上面说的第三种情况
            return False
        else:
            return True

    return False

# handle_result_json()

# print(get_result_json("api3/newcourseskill","sucess"))