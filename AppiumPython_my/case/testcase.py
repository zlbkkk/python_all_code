# # coding=utf-8
# import sys
#
# sys.path.append("E:/Teacher/Imooc/AppiumPython")
# import unittest
# import multiprocessing  #多进程
# from util.server import Server
# import time
# from business.login_business import LoginBusiness
# from util.write_user_command import WriteUserCommand
#
#
# class ParameTestCase(unittest.TestCase):
#     def __init__(self, methodName='runTest', parame=None):
#         super(ParameTestCase, self).__init__(methodName)
#         global parames
#         parames = parame
#
#
# class CaseTest(ParameTestCase):
#     @classmethod
#     def setUpClass(cls):
#
#         cls.login_business = LoginBusiness(parames)
#
#        # cls.login_business = LoginBusiness(parames)
#
#     def setUp(self):
#         print("this is setup\n")
#
#     def test_01(self):
#         print("test case 里面的参数", parames)
#         self.login_business.login_pass()
#
#     # @unittest.skip("CaseTest")
#     def test_02(self):
#         self.login_business.login_user_error()
#         print("this is case02\n")
#         self.assertTrue(True)
#
#     def tearDown(self):
#         time.sleep(1)
#         print("this is teardown\n")
#
#         # if sys.exc_info()[0]:
#         #     self.login_business.login_handle.login_page.driver.save_screenshot("../jpg/test02.png")
#
#     @classmethod
#     def tearDownClass(cls):
#         time.sleep(1)
#         print("this is class teardown\n")
#
#     # cls.driver.quit()
#
# #实例化server，也就是启动appium-server
# def appium_init():
#     server = Server()
#     server.main()
#
#
#
# def get_suite(i):
#     print("get_suite里面的", i)
#
#     suite = unittest.TestSuite()
#     suite.addTest(CaseTest("test_02", parame=i))
#     suite.addTest(CaseTest("test_01", parame=i))
#
#     unittest.TextTestRunner().run(suite)
#     # html_file = "E:/report" + str(i) + ".html"
#     # fp = open(html_file, "wb")
#     # HTMLTestRunner.HTMLTestRunner(stream=fp).run(suite)
#
# def get_count():
#     '''
#     统计userconfig.yaml有多少行数据，也就是代表着有多少个设备，为下面多进程，要起多少个进程做准备
#
#     '''
#     write_user_file = WriteUserCommand()
#     count = write_user_file.get_file_lines()
#     return count
#
#
#
#
# if __name__ == '__main__':
#     appium_init()
#     threads = []
#     # for i in range(get_count()):
#     #     print(i)
#     #
#     #     # t = threading.Thread(target=get_suite, args=(i,)) # 多线程、多台设备执行多个用例时，有可能会串，会乱，这时用多进程方式 multiprocessing
#     #     t = multiprocessing.Process(target=get_suite, args=(i,))
#     #     threads.append(t)
#     # for j in threads:
#     #     j.start()
#
#
#
#
