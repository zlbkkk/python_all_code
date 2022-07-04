from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# import sys
# # reload(sys)
# sys.setdefaultencoding('utf-8')

def browser(browser='chrome'):
    #打开浏览器，chrom\firefox\IE
    try:
        if browser=='chrome':
            driver=webdriver.Chrome()

            return driver
        elif browser=='firefox':
            driver=webdriver.Firefox()
            return driver
        elif browser=='ie':
            driver=webdriver.Ie()
            return driver
        else:
            print("Not found browser")
    except Exception as msg:
        print("%s"%msg)


# driver = browser()

class base_page(object):
    def __init__(self):
        self.driver = browser()
        self.driver.save_screenshot()



    def open_browser(self,url):
        self.driver.get(url)
        self.driver.maximize_window()


    def find_element_1(self,locator):

        return self.driver.find_element(*locator)
        # return driver.find_element_by_id(locator)


    def find_element(self,locator,timeout=10):
        '''
        定位元素
        usage:
        driver=base_page()
        locator=('id','xxx')
        driver.find_element(locator)
        '''
        elment=WebDriverWait(self.driver,10,1).until(EC.presence_of_element_located(locator))
        return elment

    def find_elemnts(self,locator,timeout=10):
        #定位一组元素
        elements=WebDriverWait(self.driver,timeout,1).until(EC.presence_of_all_elements_located)
        return elements

    def click(self,locator):
        '''
        点击元素
        usage:
        driver=base_page()
        locator=('id','xxx')
        driver.click(locator)

        '''
        element=self.find_element(locator)
        element.click()

    def send_keys(self,locator,text):
        '''
        输入文本
        usage
        driver=base_page()
        driver.send_keys(locator)
        '''
        element=self.find_element_1(locator)
        element.clear()
        element.send_keys(text)

    def is_text_in_element(self,locator,text,timeout=10):
        '''判断文本是否在元素里，返回布尔值
        usage:
        result=driver.is_text_in_elment(locator,text)

        '''
        try:
            result=WebDriverWait(self.driver,timeout,1).until(EC.text_to_be_present_in_element(locator,text))
        except TimeoutException:
            print("元素没有定位到："+str(locator))
            return False
        else:
            return result

    def is_text_in_value(self,locator,value,timeout=10):
        '''判断是否定位到元素的value值，返回布尔值
        result=driver.text_in_elemnt_value(locator,text)
        '''
        try:
            result=WebDriverWait(self.driver,timeout,1).\
                until(EC.text_to_be_present_in_element_value(locator,value))
        except TimeoutException:
            print("元素没有定位到")
            return False
        else:
            return result

    def is_title(self,title,timeout=10):
        '''判断标题完全包含'''
        result=WebDriverWait(self.driver,timeout,1).until(EC.title_is(title))
        return title

    def is_title_contains(self,title,timeout=10):
        '''判断是否包含标题'''
        result=WebDriverWait(self.driver,title).until(EC.title_contains(title))
        return result

    def is_select(self,locator,timeout=10):
        '''判断元素是否被选中，返回布尔值'''
        result=WebDriverWait(self.driver,timeout).until(EC.element_located_to_be_selected(locator))
        return result

    def alter_is_parent(self,timeout):
        '''有alter时返回alter，不适True，没有alter时返回False'''
        result=WebDriverWait(self.driver,timeout).until(EC.alert_is_present())
        return result

    def move_to_element(self,locator):
        '''鼠标悬浮操作
        usage:
        a=base_page()
        locator=('id','xxx')
        a.move_to_element(locator)

        '''
        element=self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def back(self):
        '''浏览器后退一步'''
        self.driver.back()

    def forward(self):
        '''浏览器前进一步'''
        self.driver.forward()

    def close(self):
        '''关闭浏览器'''
        self.driver.close()

    def get_tite(self):
        '''获取标题'''
        return self.driver.title

    def get_text(self):
        element=self.driver.find_element()
        return element.text

    def get_attribute(self,locator,name):
        '''获取属性'''
        result=self.driver.find_element(locator)
        return result.get_attribute(name)

    def js_excute(self,js):
        return self.driver.execute_script(js)

    def js_scroll_top(self):
        js='window.scrollTo(0,0)'
        self.driver.execute_script(js)

    def js_scroll_end(self):
        js='window.scrollTo(0,document.body.scrollHeight)'
        self.driver.execute_script(js)

    def select_by_index(self,locator,index):
        element=self.driver.find_element(locator)
        Select(element).select_by_index(index)

    def select_by_value(self,locator,value):
        element=self.driver.find_element(locator)
        Select(element).select_by_value(value)

    def select_by_text(self,locator,text):
        element=self.driver.find_element(locator)
        Select(element).select_by_visible_text()











    