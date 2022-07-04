import configparser
import os



# parent_dir = os.path.dirname(os.path.abspath(__file__))
# print(parent_dir)
# p = os.path.join(parent_dir,"LocalElement.ini")
# print(p)

base_path=os.path.dirname(os.getcwd())


class ReadIni:
    def __init__(self,file_path=None):
    #注意：file_path是传进来的，self.file_path是全局的，两个不同的
        if file_path==None:
            self.file_path= base_path+'\config\LocalElement.ini'

        else:

            self.file_path=file_path

        self.data = self.read_ini() #接收下面read_ini函数返回的对象，并在这里就初始化了

    #初始化configparser对象，并返回
    def read_ini(self):
        read_ini = configparser.ConfigParser()
        read_ini.read(self.file_path)  #这个file_path是在上面__init__传进来的
        return read_ini

    def get_value(self,key,section=None):
        if section==None:
            section = "login_element"
# try是异常处理，假设传进来的section是错的，不这样的话就会报错，现在错的话会返回None
        try:
            value = self.data.get(section,key)

        except:
            value = None
        return value  # 返回，如： id>cn.com.open.mooc:id/tvPassLogin

if __name__=='__main__':

    read_ini=ReadIni()
    a = read_ini.get_value('login_button')  #要注意先传key，再传section
    print(a)




