#coding:utf-8
#coding:utf-8
from selenium import webdriver
from Base_page.base_page import base_page
import time
from Log.log import log_setup

class loginpage(base_page):
    username_loc = ("id","fm-login-id")  #用户名框定位
    password_loc = ('id','fm-login-password')  #密码框定位
    sumit_loc=('css',".fm-button fm-submit password-login")  #登录按钮定位
    foget_pwd=('link text','忘记密码')
    register=('link text','免费注册')
    qiehuan_login=('id','J_Quick2Static')

    def input_username(self,username):
        self.send_keys(self.username_loc,username)
        # base.send_keys(self.username_loc,username)


    def input_password(self,password):
        self.send_keys(self.password_loc,password)
        # base.send_keys(self.password_loc,password)

    def click_qiehuan(self):
        '''点击切换密码登录'''
        self.click(self.qiehuan_login)
        # base.click(self.qiehuan_login)

    def click_sumit(self):
        '''点击登录按钮'''
        self.click(self.sumit_loc)
        # base.click(self.sumit_loc)

    def login(self,username,password):
        # self.click_qiehuan()
        self.driver.implicitly_wait(10)
        self.input_username(username)
        self.input_password(password)
        self.click_sumit()

