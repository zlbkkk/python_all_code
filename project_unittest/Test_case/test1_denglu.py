#coding:utf-8
from selenium import webdriver
import unittest
from Log.log import log_setup
from Data_ini.read_data import readdata
from Base_page.base_page import base_page
from Excel_data.excel_data_read import ExcelUtil
import ddt
from Page.page_denglu import loginpage


ini=readdata()
testdata=ExcelUtil("E:\\project_unittest\\Data_ini\\test.xlsx","Sheet1").dict_data()
# print testdata
Loger=log_setup('test1_denglu').getlog()

@ddt.ddt
class case_denglu(unittest.TestCase):
    def setUp(self):
        # self.driver=webdriver.Chrome()
        # self.driver.get("https://login.taobao.com")
        # self.driver.maximize_window()
        self.base=base_page()
        self.base.open_browser("https://login.taobao.com")

        Loger.info('打开网页')
        # self.driver.implicitly_wait(10)
        # self.basepage = base_page(self.driver)
        self.pg_denglu=loginpage()

    @ddt.data(*testdata)
    def test01(self,testdata):
        u'''淘宝登录'''
        self.pg_denglu.login(testdata["username"],testdata["pwd"])

        Loger.info('test01:登录淘宝')

    def tearDown(self):
        self.base.close()

if __name__=='__main__':
    unittest.main()