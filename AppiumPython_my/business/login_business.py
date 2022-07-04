from handle.login_handle import LoginHandle

class LoginBusiness:
    def __init__(self,i):
        self.login_handle = LoginHandle(i)

    def login_pass(self):
        '''登录成功的case'''
        self.login_handle.click_pass_login()
        self.login_handle.send_username("18680687654")
        self.login_handle.send_password("888888")
        self.login_handle.click_login()

    def login_user_error(self):
        '''登录失败的case'''
        self.login_handle.click_pass_login()
        self.login_handle.send_username("18680687655")
        self.login_handle.send_password("999999")
        self.login_handle.click_login()
        user_flag = self.login_handle.get_fail_tost("账号未注册")
        if user_flag:
            return True
        else:
            return False



