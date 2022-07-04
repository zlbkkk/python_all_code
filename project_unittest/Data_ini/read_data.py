#coding:utf-8
import configparser
config=configparser.ConfigParser()
config.read("c:\\project_test-1\\Data_ini\\data.ini")
class readdata:
    def sch1(self):
        sch1=config.get("search","search1")
        return sch1
    def sch2(self):
        sch2=config.get("search","search2")
        return sch2

