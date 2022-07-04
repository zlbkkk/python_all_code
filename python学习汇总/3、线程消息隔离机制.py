import threading

local_data = threading.local()
local_data.name = "local_data"


class MyThread(threading.Thread):
    def run(self):

        print("赋值前-子线程：",threading.local)


