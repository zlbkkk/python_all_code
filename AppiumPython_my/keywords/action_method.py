#封装excel中用到的关键字方法
from util.get_by_local import GetByLocal
from base.base_driver import BaseDriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ActionMethod:

    def __init__(self,driver):
        base_driver = BaseDriver()
        self.driver = base_driver.android_driver(0)

        self.get_by_local = GetByLocal(self.driver) #需要传进driver

    def input(self,*args):
        '''
        输入值的函数/关键字，excel中的“步骤”列用到

        '''
        elemnet = self.get_by_local.get_element(args[0])
        if elemnet == None:
            return args[0],"元素没找到"
        else:
            elemnet.send_keys(args[1])


    def on_click(self,*args):
        '''
        元素点击关键字

        '''
        elemnet = self.get_by_local.get_element(args[0])
        if elemnet == None:
            return args[0],"元素没找到"
        else:
            elemnet.click()

    def sleep_time(self,*args):
        time.sleep(int(args[0]))

    # 获取屏幕的宽高
    def get_size(self,*args):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width, height

    # 向左边滑动
    def swipe_left(self,*args):
        # [100,200]
        x1 = self.get_size()[0] / 10 * 9
        y1 = self.get_size()[1] / 2
        x = self.get_size()[0] / 10
        self.driver.swipe(x1, y1, x, y1, 2000)

    # 向右边滑动
    def swipe_right(self,*args):
        # [100,200]
        x1 = self.get_size()[0] / 10
        y1 = self.get_size()[1] / 2
        x = self.get_size()[0] / 10 * 9
        self.driver.swipe(x1, y1, x, y1, 2000)

    # 向上滑动
    def swipe_up(self,*args):
        # [100,200]direction
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10 * 2
        y = self.get_size()[1] / 10*2
        self.driver.swipe(x1, y1, x1, y, 1000)

    # 向下滑动
    def swipe_down(self,*args):
        # [100,200]
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10
        y = self.get_size()[1] / 10 * 9
        self.driver.swipe(x1, y1, x1, y)

    def swipe_on(self,direction):
        if direction == 'up':
            self.swipe_up()
        elif direction == 'down':
            self.swipe_down()
        elif direction == 'left':
            self.swipe_left()
        else:
            self.swipe_right()

    def get_element(self,*args):
        '''
        查找元素,也就是查找这个元素的定位信息，
        会传入一个比如username的key，然后就可以找到username key值对应的
        定位信息

        '''
        elemnet = self.get_by_local.get_element(args[0]) #会返回一个key，然后在get_element()函数中，通过这个键值找到value，也就是元素的定位信息
        if elemnet == None:
            return None

        return elemnet

    def get_tost_element(self,*args):
        '''
        获取tost的文字

        '''
        time.sleep(2)
        tost_element = ("xpath", "//*[contains(@text,"+args[0]+")]")
        WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located(tost_element))
