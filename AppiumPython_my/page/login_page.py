from util.get_by_local import GetByLocal
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from base.base_driver import BaseDriver



class LoginPage:

    def __init__(self,i):
        base_driver = BaseDriver()  #这个是真正的driver
        self.driver = base_driver.android_driver(i)  #实例化base_driver.py中的android_driver，这是一个真正的driver
        self.get_by_local = GetByLocal(self.driver)

    # 获取登录界面所有的页面元素信息
    def get_username_element(self):

        return self.get_by_local.get_element('username')

    '''获取密码元素信息'''
    def get_password_element(self):
        return self.get_by_local.get_element('password')

    '''获取"账号密码登录"按钮元素信息'''
    def get_pass_login_element(self):
        '''点击切换为"账号密码登录"的那个按钮'''
        return self.get_by_local.get_element('pass_login')

    def get_click_login_element(self):
        return self.get_by_local.get_element("login_button")

    '''获取忘记密码元素信息'''
    def get_foget_password_elemnet(self):
        return self.get_by_local.get_element('forget_password')

    def get_register_element(self):
        return self.get_by_local.get_element('register')

    def get_tost_element(self,message):
        time.sleep(2)
        tost_element = ("xpath", "//*[contains(@text,"+message+")]")
        WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located(tost_element))



