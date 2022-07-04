# coding=utf-8
import sys
import os
import configparser

base_path = os.path.dirname(os.getcwd())
sys.path.append(base_path)


class HandleInit:

    def load_ini(self):
        file_path = base_path + "/Config/server.ini"
        # print(file_path)
        cf = configparser.ConfigParser()
        cf.read(file_path, encoding="utf-8-sig")
        return cf

    def get_value(self,key,node=None):
        '''
        获取ini里面的value ,这个是在base_request.py中的run_main()中有调用
        '''

        cf = self.load_ini()

        if node==None:
            node="server"


        try:
            data = cf.get(node, key)
        except Exception:
            print("没有获取到值")
            data = None
        return data


# if __name__ == "__main__":
#     hi = HandleInit()
#     print(hi.get_value("password"))