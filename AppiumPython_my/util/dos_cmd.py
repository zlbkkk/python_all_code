#作用：执行cmd命令的类
import os
# print(os.system('adb devices')) #只会打印，不会收集结果
#
# os.popen('adb devices').readlines()  #读取结果，是一个list

class DosCmd:

    #执行一个cmd命令，并返回结果
    def excute_cmd_result(self,command):
        result_list = []

        # ['List of devices attached\n', '127.0.0.1:7555\tdevice\n', '\n']
        result = os.popen(command).readlines()  # 读取结果，是一个list: 如上

        for i in result:

            if i == '\n':
                continue
            result_list.append(i.strip('\n'))

        return result_list # 返回如：['List of devices attached', '127.0.0.1:7555\tdevice']


        '''
            说明：
            strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
            该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
        '''

    def excute_cmd(self,command):
        os.system(command)

if __name__ =="__main__":
    dos=DosCmd()
    print(dos.excute_cmd_result("adb devices"))