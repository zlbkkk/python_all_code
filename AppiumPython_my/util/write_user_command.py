#该文件时读取yaml文件，存放设备的信息 端口等

import yaml
class WriteUserCommand():

	def read_data(self):
		'''
		#获取yaml文件数据的函数，返回全部数据

		'''
		with open("../config/userconfig.yaml") as fp:
			data = yaml.load(fp,Loader=yaml.FullLoader) # load方法转成字典
		return data

	def get_value(self,key,port):
		'''
		根据上面函数返回的数据，获取所需的value
		'''
		data = self.read_data()
		value = data[key][port]
		return value

	def write_data(self,i,device,bp,port):  #这个函数的i,device,bp,port参数和下面join_data()相呼应
		'''
		写入数据函数，在server中，有设备信息，端口，bp端口，
		需要将其写入yaml文件
		'''
		data = self.join_data(i,device,bp,port)
		with open("../config/userconfig.yaml","a") as fr:
			yaml.dump(data,fr)

	def join_data(self,i,device,bp,port):
		'''
		格式化数据写入yaml的格式，为上面的write_data()函数做服务，
		写入的格式是这样：
		user_info_0: {bp: '4916', deviceName: '127.0.0.1:21503', port: '4700'}

		'''
		data = {
			"user_info_"+str(i):{
				"devicesName":device,
				"bp":bp,
				"port":port


			}


		}

		return data


	def clear_data(self):
		'''
		清理userconfig.yaml文件的内容，因为每次运行写都是在后面增加，
		现在在每次运行之前都先清理掉上一次写入的数据，这样就避免重复

		'''
		with open("../config/userconfig.yaml","w") as fr:
			fr.truncate()  #这个方法是清理数据
		fr.close()

	def get_file_lines(self):
		'''
		获取userconfig.yaml有多少行，也就是有多少个设备信息，为起多少个线程服务
		为testcase.py所用

		'''
		data = self.read_data()
		return len(data)



if __name__ == '__main__':
	a=WriteUserCommand()
	# print(a.get_value("user_info_0","port"))
	print(a.get_file_lines())