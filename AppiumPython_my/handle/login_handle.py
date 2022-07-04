from page.login_page import LoginPage #导入page类


#操作层，调用获取元素的page层，加上对元素要进行的操作，形成操作层
class LoginHandle:
    def __init__(self,i): #类login_page.py中需要传入一个i，所以这里也要传i
        self.login_page = LoginPage(i)

    def send_username(self,user):
        '''输入用户名'''
        self.login_page.get_username_element().clear()
        self.login_page.get_username_element().send_keys(user)

    def send_password(self, password):
        '''输入密码'''
        self.login_page.get_password_element().clear()
        self.login_page.get_password_element().send_keys(password)


    def click_forget_password(self):
        '''点击忘记密码'''
        self.login_page.get_foget_password_elemnet()

    def click_pass_login(self):
        '''
        点击“账号密码登录”按钮
        '''
        self.login_page.get_pass_login_element().click()

    def click_login(self):
        self.login_page.get_click_login_element().click()

    def click_register(self):
        '''
        点击注册按钮
        :return:
        '''
        self.login_page.get_register_element()




    def get_fail_tost(self,message):
        '''
        获取tost,根据返回信息进行反数据
        :param message:
        :return:
        '''
        tost_element = self.login_page.get_tost_element(message)
        if tost_element:
            return True
        else:
            return False

