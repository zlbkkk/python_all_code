#操作excel的py文件

import xlrd
from xlutils.copy import copy  #把内容写入excel中，追加模式



class OperaExcel:

    def __init__(self,file_path=None,i=None):
        if file_path == None:
            self.file_path = "F:\AppiumPython_my\config\case.xls"
        else:
            self.file_path=file_path

        if i ==None:
            i=0

        #初始化下面这两个，让他进来就拿到是哪个sheets
        self.excel = self.get_excel()
        self.data = self.get_sheets(i)


    def get_excel(self):
        '''
        获取excel

        '''
        excel = xlrd.open_workbook(self.file_path)
        return excel

    def get_sheets(self,i):
        '''
        获取sheets的内容

        '''
        tables = self.excel.sheets()[i]
        return tables

    def get_lines(self):
        '''
        获取excel行数

        '''
        lines = self.data.nrows
        return lines

    def get_cell(self,row,cell):
        '''
        获取单元格的内容

        '''
        data = self.data.cell(row,cell).value
        return data

    def write_value(self,row,value):
        '''
        将用例的执行结果写入excel中，比如pass，fail

        '''
        read_value = self.excel #打开想要更改的excel文件
        write_data = copy(read_value) #将操作文件对象拷贝，变成可写的workbook对象

        write_save = write_data.get_sheet(0) #获得第一个sheet的对象 注意：get_sheet()是xlutils.copy自带的方法

        write_save.write(row,8,value) #写入数据
        write_data.save(self.file_path) #保存,注意excel后缀名必须是xls的




# if __name__ == "__main__":
    # opera = OperaExcel()
    # print(opera.get_lines())
    # print(opera.get_cell(7,3))
    # print(opera.write_value(6, 'zlb'))


