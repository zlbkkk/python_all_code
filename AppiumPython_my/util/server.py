#作用：获取dos_cmd文件获取的设备信息，然后在此py文件中处理
#此文件主要是生成已经处理干净的设备信息和端口


from util.dos_cmd import DosCmd
from util.port import Port
import threading
from util.write_user_command import WriteUserCommand
import time


class Server:
    def __init__(self):
        self.dos = DosCmd()
        self.device_list = self.get_devices()  #这个会返回设备的列表.也就是self.device_list等于设备列表
        self.write_file = WriteUserCommand()

    def get_devices(self):
        '''
        获取设备信息，获取到的信息如：
        127.0.0.1:21503，会将这个放入devices_list中存放

        '''
        devices_list = []
        result_list = self.dos.excute_cmd_result('adb devices')

        '''先判断list有没有数值，没有的话去循环就会报错，所以先做一个判断'''
        if len(result_list)>=2:  #因为list中第一个默认是：List of devices attached，往后才是真正的设备信息，所以要>=2
            for i in result_list:
                if 'List' in i:
                    continue
                devices_info = i.split('\t') # 分割127.0.0.1:21503\tdevices
                if devices_info[1] == 'device': #等于devices设备信息才有效，有时候会是其他的
                    devices_list.append(devices_info[0])  #此时会把 127.0.0.1:21503加入到list中
            return devices_list #返回这样的：[127.0.0.1:21503]


        else:
            return None

    def create_port_list(self,start_port):
        '''
        调用port.py中的Port类的create_port_list函数来生成可用端口
        并将端口放入port_list中
        '''
        port = Port()
        port_list = []
        port_list = port.create_port_list(start_port,self.device_list) #调用create_port_list会先判断端口是否可用
        return port_list

    def create_command_list(self,i):
        '''
            #特别注意：参数i的数值由设备数决定，在下面的main()函数中有体现，i的值决定着生成多少个appium ...命令，
            也就是len(get_devices函数返回的列表的个数），在下面的main()中才传入)

            #生成如这样的命令：[appium -p 4700 -bp 4701 -u 127.0.0.1:21503]
            并将命令放入command_list中

        '''

        command_list = []   #存放启动命令的list，如上 appium ... ...
        appium_port_list = self.create_port_list(4700)
        bootstrap_port_list = self.create_port_list(4900)
        devices_list = self.device_list #获取设备列表，已在__init__中初始化
        # command = "appium -p "+str(appium_port_list[i])+" -bp "+\
        #                         str(bootstrap_port_list[i])+" -U "+devices_list[i]+\
        #                         " --no-reset --session-override"
        command = "appium -p " + str(appium_port_list[i]) + " -bp " + str(bootstrap_port_list[i]) + " -U " + \
                  devices_list[i] + " --no-reset --session-override"
        command_list.append(command)

# 下面这个self.write_file.write_data是将设备信息写入yaml文件，调用的是write_user_command.py中的write_data()
        self.write_file.write_data(i, devices_list[i], str(bootstrap_port_list[i]), str(appium_port_list[i]))
        return command_list

    #对command_list列表中存放的命令，一一进行启动
    def start_server(self,i):  #传i表示控制执行list中的哪一个
        self.start_list = self.create_command_list(i)   #获取启动命令,如：[appium -p 4700 -bp 4701 -u 127.0.0.1:21503]
        print(self.start_list)
# 下面这句：调用dos_cmd中excute_cmd函数执行dos命令，但是目前只有一个线程，一个线程只能启动一个命令，所以需要用到多线程，下面的main()函数
        self.dos.excute_cmd(self.start_list[0])
        '''
    针对上一行: self.dos.excute_cmd(self.start_list[0]) 中的0的解释：
    这个self.start_list[0]视频解说约在1:34:00处，start_list表示命令列表，在main()中，每次启动一个线程时，他会去调生成
    命令的函数create_command_list()生成一个命令 ,如：[appium -p 4700 -bp 4701 -u 127.0.0.1:21503]，
    也就是一个线程只能生成一个命令，只有一个，那就是传0，如果传i，下面main()函数的循环中，i会根据设备数量不断加大，有可能是1 2 3
    那就会报“超出边界的错误”
    
        '''

#再定义一个函数，多线程对上面的start_server函数执行启动命令
    def main(self):
        thread_list = []
        self.kill_server() #每次启动先杀掉之前的进程
        self.write_file.clear_data()  #每次运行先清理userconfig.yaml中的数据，因为每次都会追加，就会重复
        for i in range(len(self.device_list)): #self.device_list表示设备的个数，有多少个设备我就起多少个线程，从第一个函数get_devices()中获取列表
            appium_start = threading.Thread(target=self.start_server,args=(i,))
            thread_list.append(appium_start)
        for j in thread_list:
            j.start()
        time.sleep(25)

    #杀掉appium服务进程,每次执行多线程启动时,也就是执行main()时，都先杀掉
    def kill_server(self):
        server_list = self.dos.excute_cmd_result('tasklist | find "node.exe"')
        if len(server_list)>0:
            self.dos.excute_cmd('taskkill -F -PID node.exe')






# if __name__ == '__main__':
#     server = Server()
#     print(server.main())
