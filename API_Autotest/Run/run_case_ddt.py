
# 通过ddt的方式去运行用例，把excel中的全部行的内容，取到一个列表中，然后在传入

import os
import unittest
import json
import ddt
import requests
import HTMLtestRunnerScreenShot

from Util.handle_excel import HandExcel
from Base.base_request import BaseRequest
from Util.handle_ini import HandleInit
from Util.handle_result import handle_result,handle_result_json,get_result_json
from Util.handle_cookie import get_cookie_value,write_cookie
from Util.handle_header import get_header
from Util.condition_data import get_data
from Util.send_emali import send


excel_data = HandExcel()
base_path = os.path.dirname(os.getcwd())
print("路径是：---->",base_path)

data = excel_data.get_excel_data() # 数据源，excel中的全部数据
request = BaseRequest() #  实例化封装了get、post请求的类

print(data)

@ddt.ddt
class TestRunCaseDdt(unittest.TestCase):

    @ddt.data(*data)
    def test_main_case(self,data):
        cookie = None
        get_cookie = None
        header = None
        depend_data = None
        is_run = data[2]
        case_id = data[0]
        i = excel_data.get_rows_number(case_id)
        if is_run == 'yes':
            is_depend = data[3]
            data1 = json.loads(data[7])
            try:
                if is_depend:
                    '''
                    获取依赖数据
                    '''
                    depend_key = data[4]
                    depend_data = get_data(is_depend)
                    # print(depend_data)
                    data1[depend_key] = depend_data

                method = data[6]
                url = data[5]

                is_header = data[9]
                excepect_method = data[10]
                excepect_result = data[11]
                cookie_method = data[8]

                if cookie_method == 'yes':
                    cookie = get_cookie_value('app')
                if cookie_method == 'write':
                    '''
                    必须是获取到cookie
                    '''
                    get_cookie = {"is_cookie": "app"}
                if is_header == 'yes':
                    header = get_header()

                res = request.run_main(method, url, data1, cookie, get_cookie, header)
                # print(res)
                code = str(res['errorCode']) # 对返回结果，通过字典方式获取errorcode
                message = res['errorDesc']
                # message+errorcode

                if excepect_method == 'mec':  # 通过接口返回的错误信息描述和维护在json文件的错误信息描述作对比
                    config_message = handle_result(url, code) # 获取到json文件中的“错误信息描述”
                    '''
                        if message == config_message:
                            excel_data.excel_write_data(i,13,"通过")
                        else:
                            excel_data.excel_write_data(i,13,"失败")
                            excel_data.excel_write_data(i,14,json.dumps(res))
                    '''
                    try:
                        self.assertEqual(message, config_message)
                        excel_data.excel_write_data(i, 13, "通过")  # 这里的i和run_main.py中的run_case()里面的i不同，这里是直接就获取到了行号，那边是for循环，i从0开始
                        excel_data.excel_write_data(i, 14, json.dumps(res))
                    except Exception as e:
                        excel_data.excel_write_data(i, 13, "失败")
                        excel_data.excel_write_data(i + 2, 14, json.dumps(res))  # 将结果写入到excel的 “数据”单元格中
                        raise e

                if excepect_method == 'errorcode':
                    '''
                    if excepect_result == code:
                        excel_data.excel_write_data(i,14,"通过")
                    else:
                        excel_data.excel_write_data(i,13,"失败")
                        excel_data.excel_write_data(i,14,json.dumps(res))
                    '''
                    try:
                        self.assertEqual(excepect_result, code)
                        excel_data.excel_write_data(i, 13, "通过")
                        excel_data.excel_write_data(i + 2, 14, json.dumps(res))  # 将结果写入到excel的 “数据”单元格中
                    except Exception as e:
                        excel_data.excel_write_data(i, 13, "失败")
                        excel_data.excel_write_data(i + 2, 14, json.dumps(res))  # 将结果写入到excel的 “数据”单元格中
                        raise e

                if excepect_method == 'json':

                    if code == 1000:
                        status_str = 'sucess'
                    else:
                        status_str = 'error'
                    excepect_result = get_result_json(url, status_str)
                    result = handle_result_json(res, excepect_result)
                    '''
                    if result:
                        excel_data.excel_write_data(i,13,"通过")
                    else:
                        excel_data.excel_write_data(i,13,"失败")
                        excel_data.excel_write_data(i,14,json.dumps(res))   
                    '''
                    try:
                        self.assertTrue(result)
                        excel_data.excel_write_data(i, 13, "通过")
                        excel_data.excel_write_data(i + 2, 14, json.dumps(res))  # 将结果写入到excel的 “数据”单元格中
                    except Exception as e:
                        excel_data.excel_write_data(i, 13, "失败")
                        excel_data.excel_write_data(i + 2, 14, json.dumps(res))
                        raise e
            except Exception as e:
                excel_data.excel_write_data(i, 13, "失败") # 整个代码体如果失败会执行这个except下的代码，那就意味这用例也是失败的
                excel_data.excel_write_data(i + 2, 14, json.dumps(res))  # 将结果写入到excel的 “数据”单元格中
                raise e

if __name__=="__main__":

    case_path = base_path + "/Run"
    report_path = base_path + "/report/report.html"
    discover = unittest.defaultTestLoader.discover(case_path, pattern="run_case_*.py")
    # unittest.TextTestRunner().run(discover)
    with open(report_path, "wb") as f:
        runner = HTMLtestRunnerScreenShot.HTMLTestRunner(stream=f, title="最棒QA", description="this is zlb")
        runner.run(discover)

    # send()