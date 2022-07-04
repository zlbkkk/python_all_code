import threading

cond = threading.Condition()

class kongbaige(threading.Thread):

    def __init__(self,cond,name):
        threading.Thread.__init__(self,name=name)
        self.cond = cond


    def run(self):
        self.cond.acquire()