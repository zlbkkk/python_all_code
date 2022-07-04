#coding=utf-8
import sys
sys.path.append("F:\AppiumPython_my")
import unittest
import HTMLTestRunner
import threading
import multiprocessing
from util.server import Server
import time,os
from appium import webdriver
from business.login_business import LoginBusiness
from util.write_user_command import WriteUserCommand
from page.login_page import LoginPage

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib



class ParameTestCase(unittest.TestCase):
	def __init__(self,methodName='runTest',parame=None):
		super(ParameTestCase,self).__init__(methodName)
		global parames
		parames = parame

class CaseTest(ParameTestCase):
	@classmethod
	def setUpClass(cls):
		print("=================执行开始==================")
		print("setUpclass---->",parames)
		cls.login_business = LoginBusiness(parames)

	# def setUp(self):
	#
	# 	print("this is setup\n")


	def test_01(self):
		print("test case 里面的参数",parames)
		self.login_business.login_pass()


		#self.assertNotEqual(1,2)
		#self.assertTrue(flag)
		#self.assertFalse(flag)
	#@unittest.skip("CaseTest")
	def test_02(self):
		self.login_business.login_user_error()
		print("this is case02\n")
		self.assertTrue(True)
	# def tearDown(self):
	# 	time.sleep(1)
	# 	print("this is teardown\n")
		# if sys.exc_info()[0]:
		# 	self.login_business.login_handle.login_page.driver.save_screenshot("../jpg/test02.png")


		
	@classmethod
	def tearDownClass(cls):
		print("=================执行结束==================")
		time.sleep(1)
		cls.login_page = LoginPage(parames)
		cls.login_page.quit()
		print("this is class teardown\n")
		#cls.driver.quit()

def appium_init():
	server = Server()
	server.main()


def get_suite(i):
	print("get_suite里面的", i)
	suite = unittest.TestSuite()
	suite.addTest(CaseTest("test_02", parame=i))
	suite.addTest(CaseTest("test_01", parame=i))

	# unittest.TextTestRunner().run(suite)
	html_file = "E:\\project_unittest\\report.html"
	fp = open(html_file, "wb")
	HTMLTestRunner.HTMLTestRunner(stream=fp).run(suite)


def get_count():
	write_user_file = WriteUserCommand()
	count = write_user_file.get_file_lines()
	return count





if __name__ == '__main__':
	appium_init()
	#get_suite(0)
	# threads = []
	# for i in range(get_count()): # 这个i是获取yaml文件中的哪一个，如：user_info_0
	# 	print (i)
	# 	t = multiprocessing.Process(target=get_suite,args=(i,))
	# 	threads.append(t)
	# for j in threads:
	# 	j.start()


# if __name__ == '__main__':
# 	appium_init()
# 	#get_suite(0)
# 	threads = []
# 	for i in range(get_count()):
# 		print(i)
# 		t = multiprocessing.Process(target=get_suite,args=(i,))
# 		threads.append(t)
# 	for j in threads:
# 		j.start()




	# report_path = 'E:\\unittest_report\\'  # 用例文件夹
	# report_file = get_report_file(report_path)  # 3获取最新的测试报告
	#
	# sender = "18680674921@163.com"
	# psw = "JUBMSUDZGUVSHKYF"  # 不是你邮箱的密码，看此链接：https://blog.csdn.net/wateryouyo/article/details/51766345
	# smtp_server = "smtp.163.com"
	# port = 465
	# receiver = "1315392407@qq.com"  # 接收者的邮箱
	# send_mail(sender, psw, receiver, smtp_server, report_file, port)  # 4最后一步发送报告
