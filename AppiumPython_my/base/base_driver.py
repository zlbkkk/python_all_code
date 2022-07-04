#统一生成driver，整个项目的driver都源于此
import time
from appium import webdriver
from util.write_user_command import WriteUserCommand

class BaseDriver:

    # i的作用主要是用来取yaml文件中的那个user_info的
    def android_driver(self,i): #i的作用是区分yaml文件中的最外层的键值如这个0---->  user_info_0:
        write_file = WriteUserCommand()
        devices = write_file.get_value("user_info_"+str(i),"devicesName") #因为键值user_info_0后面的0是会变化的 0  1 2，所以不要写死，后面i是行数,从 login_page.py开始传
        port = write_file.get_value("user_info_"+str(i),"port")
        capabilities = {
                    "platformName": "Android",
                    # "automationName":"UiAutomator2",
                    "deviceName": devices,
                    # "app": "E:\\ziliao\\mukewang.apk",
                    "appPackage":"cn.com.open.mooc",
                    "appActivity":"cn.com.open.mooc.component.user.activity.login.LoginActivity",
                    # "appWaitActivity":"cn.com.open.mooc.user.login.MCLoginActivity",
                    "noReset": "true"
                }
        driver = webdriver.Remote("http://127.0.0.1:"+port+"/wd/hub", capabilities)
        time.sleep(10)
        return driver



    def ios_driver(self):
        pass

