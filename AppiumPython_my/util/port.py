#作用：生成可用的端口 port
from util.dos_cmd import DosCmd
class Port:
    #检测端口是否被占用的函数
    def port_is_uesd(self,port_num):
        flag = None
        self.dos = DosCmd()
# 检查端口是否被占用：netstat -ano | findstr 8080 ，如果占用了会返回结果，没占用就返回空
        command = "netstat -ano | findstr "+str(port_num)  #整型和字符串不能拼接，要转换成字符串
        result = self.dos.excute_cmd_result(command)
        if len(result) > 0:  #判断result是否有数值，有数值代表端口被占用
            flag = True
        else:
            flag = False
        return flag

    # 生成可用的端口的函数
    def create_port_list(self,start_port,devices_list):
        port_list = []
        if devices_list != None: #根据server.py中的devices_list()函数的返回判断，不等于None才去生成下面的端口，等于None代表没有设备信息
            '''
            从start_port开始，循环生成可用的port
            本来要用for循环，循环次数等于设备的个数，也就是列表的个数，如：for i in range(len(devices_list)):
            但是，如果循环的时候，port已被占用，则此时这个port就无效，但是for循环因为只循环和
            devices个数相等的次数，所以就可能会造成少生成port，因为端口被占用后，该端口就不生成了，
            但是for循环的次数是固定的，所以应该用while循环
                        
            '''
            while len(port_list) != len(devices_list):
                if self.port_is_uesd(start_port) != True:  #调用port_is_uesd()函数，判断端口是否可用，等于True表示端口被占用
                    port_list.append(start_port)
                start_port = start_port + 1   #端口大小不断加1，看是否被占用
            return port_list

        else:
            print("生成可用端口失败")
            return None



if __name__ == '__main__':


	port = Port()
    #使用示例，要穿一个start_port和一个设备的list
	li = [1,2,3,4,5]
	print(port.create_port_list(4722,li))





