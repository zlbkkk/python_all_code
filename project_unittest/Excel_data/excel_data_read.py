#coding:utf-8

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import ddt
import xlrd
import unittest
from Log.log import log_setup
Loger=log_setup('excel_data_read').getlog()
# import xdrlib ,sys

class ExcelUtil():
    def __init__(self, excelPath, sheetName):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j=1
            for i in range(self.rowNum-1):
                s = {}
                # 从第二行取对应values值
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j+=1
            return r





# if __name__=='__main__':
#     filepath = "C:\\test.xlsx"
#     sheetName = "Sheet1"
#     data = ExcelUtil(filepath, sheetName)
#     print(data.dict_data())

# def xunhuan():
#     list_data=excel_table_byindex("c:\\test.xlsx",0)
#     for i in range(len(list_data)):
#         # print list_data[i]['username']
#         # print list_data[i]['password']
#         # return list_data[i]['username'],list_data[i]['password']
#         return list_data



# def Login():
#
#     listdata = excel_table_byindex("c:\\test.xlsx", 0)
#     # rowone_num = listdata.row_values()
#     if (len(listdata) <= 0):
#         assert 0, u"Excel数据异常"
#
#
#     broswer = webdriver.Chrome()
#     broswer.get("http://bbc.k3cloud.kingdee.com/")
#     # assert "effevo" in broswer.title
#     broswer.maximize_window()
#
#     # 点击登录按钮
#     broswer.find_element_by_id('userName').send_keys(listdata[i]['username'])
#     # Loger.info("输入用户名%s"%'u'(listdata[i]['username']))
#     broswer.find_element_by_id('password').send_keys(listdata[i]['password'])
#     # Loger.info("输入密码%s"%listdata[i]['password'])
#     broswer.find_element_by_id('submit').click()
#     time.sleep(2)
#     try:
#         # Loger.info("验证用户%s是否登录成功"%listdata[i]['username'])
#         elm = broswer.find_element_by_xpath("//a[contains(text(),'Hi')]")
#     except NoSuchElementException:
#         assert 0, u"登录失败"
#     broswer.close()

# if __name__ == '__main__':
#     # a=excel_table_byindex("c:\\test.xlsx",0)
#     Login()

