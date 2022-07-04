#coding:utf-8
import logging
#设置一个Loger
class log_setup():
    def __init__(self,loger):
        self.loger=logging.getLogger(loger)
        #设置日志级别
        self.loger.setLevel(logging.INFO)
        #创建日志格式
        self.formatter=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')

        #输出到日志文件
        fh = logging.FileHandler('E:\\project_unittest\\Log\\log_data.txt','a+',encoding="utf-8")
        fh.setLevel(logging.INFO)
        fh.setFormatter(self.formatter)

        # 输出到控制台
        sh = logging.StreamHandler()
        sh.setLevel(logging.INFO)
        sh.setFormatter(self.formatter)

        # 把Hangdle输出到loger
        self.loger.addHandler(fh)
        self.loger.addHandler(sh)
    def getlog(self):
        return self.loger

# 日志级别：
# critical > error > warning > info > debug, notset
# 级别越高打印的日志越少，反之亦然，即
# debug: 打印全部的日志(notset等同于debug)
# info: 打印info, warning, error, critical级别的日志
# warning: 打印warning, error, critical级别的日志
# error: 打印error, critical级别的日志
# critical: 打印critical级别
# '''













