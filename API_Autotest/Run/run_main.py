import os
import unittest
import json
# import HTMLtestRunnerScreenShot
import HTMLTestRunner_old
from Util.handle_excel import HandExcel
from Base.base_request import BaseRequest
from Util.handle_ini import HandleInit
from Util.handle_result import handle_result,handle_result_json,get_result_json
from Util.handle_cookie import get_cookie_value,write_cookie
from Util.handle_header import get_header
from Util.condition_data import get_data

base_path = os.path.dirname(os.getcwd())


excel_data = HandExcel() # 实例化操作excel的类
request = BaseRequest() #  实例化封装了get、post请求的类
handle_ini = HandleInit() # 实例化操作ini的类

class RunMain:

    def run_case(self):
        rows = excel_data.get_rows()

        for i in range(rows):

        #  cookie = None ，表示是否携带cookie,先给cookie赋一个None值，这个cookie赋值要放在这里，不能放在for循环外，
        # 要不然会所有的用例都带上cookie，放在这里意思是每次循环都重置一下cookie
            cookie = None
            get_cookie=None
            header = None
            # depend_data = None


            '''
            解释1：对下面i+2的解释
                # 因为i从0开始，excel中第一行是标题，第二行才是值，所以我们要从第二行开始取值，
                第一次循环0+2=2，也就是一开始会从第二行开始取值，往下就是第3 4...行
            
            '''

            # data会返回某一行的内容，是这样的列表 ['imooc_001', '获取广告位', 'yes', None ]
            data = excel_data.get_row_value(i+2) # i+2参考：解释1
            is_run = data[2] #在列表的第三个值代表是否运行该用例


            if is_run == "yes":
                is_depend = data[3] # 获取excel中的“前置条件单元格的值”
                data1 = json.loads(data[7])  # 获取excel中“data”列，也就是请求报文,要转换为字典，下面才能对依赖的字典进行更新操作，更新：data[depend_key] = depend_data
                if is_depend:
                    '''
                    解释4：
                        1、is_depend的值为imooc_001>data.banner.[0].id，在get_data(is_depend)传入即可
                        2、depend_data的值即为依赖的值：如：{"id":"1709"},也就是1709
                        3、接下来是拿这个依赖的值取更新原case请求的报文的这个id字段的值，excel中会有一个“依赖key”的单元格写明是依赖哪个key
                    '''
                    depend_key = data[4] #获取excel中“依赖key”单元格的值，即：当前用例哪个字段依赖上一条
                    depend_data = get_data(is_depend) # 参考解释4 ，denpend_data的值为要依赖的值，is_depend传进的是imooc_001>data.banner.[0].id
                    data1[depend_key] = depend_data # 在原报文上对依赖的字段的值进行更新，更新为依赖的值



                method = data[6] # 获取列表中的请求方法是什么
                url = data[5] # 获取请求的url
                is_header = data[9] # 获取excel中的"header操作"单元格的值，看是否需要携带请求头
                except_method = data[10]  # 获取excel中的"预期结果方式"单元格的值，即：通过上面方式校验预期结果，code,josn比对等
                except_result_excel = data[11] # 获取excel中的"预期结果"单元格的值，即：写着一个正确的code
                condition = data[3] #获取excel中“前置条件”单元格的值，即：依赖哪个用例，并且写明依赖哪个字段的值

                cookie_metnod = data[8] # 获取excel中的"cookie操作"单元格的值，看是否需要携带cookie
                if cookie_metnod=="yes": #判断是否需要传入cookie，如果需要则取出cookie，并在request.run_main(method,url,data1,cookie)传入
                    cookie=get_cookie_value("app") # 获取键为app的cookie值,在base_request.py中的send_post()会用到，自己项目的cookie存到哪个键值下，到时候就写哪个

                if cookie_metnod == "write": # 是否需要些cookies
                    get_cookie = {"is_cookie":"app"} # get_cookie为什么要这样传？因为键值app可以灵活配置，有可能是其他项目，又是不同的键值，在获取的时候根据键获取即可

                if is_header == "yes":
                    header = get_header()

                '''
                解释2：
                    如果cookie_metnod == "write"，就让get_cookie有值，此时下面的request.run_main（...）
                    即：会执行base_request.py中的send_post()或send_get()函数中的 respone.cookies，转换后，cookie_value就会是cookie
                    ，并会调用 write_cookie(cookie_value,get_cookie["is_cookie"]) 函数,将cookie写入到cookie.json文件中
                    
                '''
                res = request.run_main(method,url,data1,cookie,get_cookie,header) # 参考解释2，这个run会包含将cookie写入文件的步骤


                # print(res)
                code = str(res['errorCode']) # 从接口实际执行的结果提取错误的code：{'status': 1, 'data': [], 'errorCode': 1006, 'errorDesc': 'token error', 'timestamp': 1604112542052}
                message = res["errorDesc"] # 从接口实际执行的结果提取错误的信息描述 {'status': 1, 'data': [], 'errorCode': 1006, 'errorDesc': 'token error', 'timestamp': 1604112542052}
                cofig_message = handle_result(url,code)  # 这个是拿到我们预先写入到配置文件的错误信息描述，配置文件的信息格式为： {"errorCode":"errorDesc"}
                # print(res)

                #以下三个 if except_method 分别是三种方式的断言

                if except_method == 'mec': # mec代表是通过code_message.json文件来校验结果是否正确的，校验错误信息描述

                    if message == cofig_message: # 接口返回的描述信息和code_message.json维护的描述信息进行对比，看是否通过
                        print("测试case通过")
                        excel_data.excel_write_data(i+2,13,"通过") # 将结果写入到excel的 “result”单元格中
                    else:

                        print("测试case失败")
                        excel_data.excel_write_data(i + 2, 13, "失败") # 将结果写入到excel的 “result”单元格中
                        excel_data.excel_write_data(i + 2, 14, json.dumps(res)) # 将结果写入到excel的 “数据”单元格中

                if except_method == "errorcode": # 代表通过错误码来判断预期结果
                    if except_result_excel == code: # 拿excel“预期结果”单元格填写的code与接口实际返回的code作对比，看是否通过
                        print("测试case通过")
                        excel_data.excel_write_data(i + 2, 13, "通过")  # 将结果写入到excel的 “result”单元格中
                        excel_data.excel_write_data(i + 2, 14, json.dumps(res))  # 将结果写入到excel的 “数据”单元格中
                    else:
                        print("测试case失败")
                        excel_data.excel_write_data(i + 2, 13, "失败")  # 将结果写入到excel的 “result”单元格中
                        excel_data.excel_write_data(i + 2, 14, json.dumps(res))  # 将结果写入到excel的 “数据”单元格中


                if except_method == "json":

                    '''
                        解释3：
                        因为get_result_json()要传进去一个status，这个status是sucess或者error，
                        因为慕课网的报文中成功和失败就是用sucess或error来标识的，sucess或error可以根据项目的报文来定义，
                        那现在我们怎么知道是传sucess或者error呢？那就是根据返回的code来判断
                    
                    '''
                    if code ==1000:
                        status_str = "sucess"

                    else:
                        status_str = "error"


                    excepect_result = get_result_json(url,status_str)  #参考 解释3 ,excepect_result获取到的是配置文件的报文结构

                    result = handle_result_json(res,excepect_result) # 比较两个json的不同
                    # print(result)
                    if result ==True:
                        print("测试case通过")
                        excel_data.excel_write_data(i + 2, 13, "通过")  # 将结果写入到excel的 “result”单元格中
                    else:
                        print("测试case失败")
                        excel_data.excel_write_data(i + 2, 13, "失败")  # 将结果写入到excel的 “result”单元格中
                        excel_data.excel_write_data(i + 2, 14, json.dumps(res))  # 将结果写入到excel的 “数据”单元格中


                # print(res)



if __name__=="__main__":

    case_path = base_path + "/Run"
    report_path = base_path + "/report/report.html"
    discover = unittest.defaultTestLoader.discover(case_path, pattern="run_main.py")
    # unittest.TextTestRunner().run(discover)
    with open(report_path, "wb") as f:
        runner = HTMLTestRunner_old.HTMLTestRunner(stream=f, title="Mushishi", description="this is zlb")
        runner.run(discover)