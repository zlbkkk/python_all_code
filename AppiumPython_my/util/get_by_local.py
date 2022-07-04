#简介：获取ini文件中的定位信息，返回的是元素的具体定位信息，不是键值

from util.read_init import ReadIni


class GetByLocal:
#因为没有driver，所以需要传入driver，现在这里不是真正的driver，只是在这里留一个口，等到真正有driver的py文件在填入driver就可以了
#使用例子： get_by_local = GetByLocal(driver)

    def __init__(self,driver):


        self.driver = driver

def get_element(self, key):
        read_ini = ReadIni()
        local = read_ini.get_value(key)
        print(local)
##因为上面实例化的read_ini.get_value函数，在read_init.py中的get_value函数作了判断，有可能会返回None,所以这里需要加一个判断是否等于None
        if local != None:
            by = local.split('>')[0]
            local_by = local.split('>')[1]
    # 在login_page.py调用时，传入的是这样：username=id>cn.com.open.mooc:id/account_edit1，根据前面是id或者是classname来判断是用哪种定位方式
            try:
                if by == 'id':
                    return self.driver.find_element_by_id(local_by) #返回的是一个定位到的元素，
                elif by == 'className':
                    return self.driver.find_element_by_class_name(local_by)
                else:
                    return self.driver.find_element_by_xpath(local_by)
            except:
                # self.driver.save_screenshot("../jpg/test02.png")
                return None
        else:
            return None



if __name__=='__main__':

    a=GetByLocal()
    b = a.get_element('pass_login')  #要注意先传key，再传section
    print(b)
