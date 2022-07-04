#获取excel中各个单元格的值，每个单元格的值代表不同的意思，比如：“excel中的“步骤”列代表函数名称；“元素”列代表的是元素的定位信息 ”

from util.opera_excel import OperaExcel

class GetData:

    def __init__(self):
        self.opera_excel = OperaExcel()

    def get_case_lines(self):
        '''
        获取case的行数

        '''
        lines = self.opera_excel.get_lines()
        return lines

    def get_handle_step(self,row):
        '''
        获取操作步骤里面的操作方法的名字，也就是我们封装的关键字，在action_method.py中

        '''
        method_name = self.opera_excel.get_cell(row,3) #因为步骤，也就是我们封装的关键字是在excel中的第3列中用到，所以固定写死
        return method_name

    def get_element_key(self,row):
        '''
        获取操作元素的key，在LocalElement.ini中
        '''
        '''
        这个函数是获取excel中"元素"那一列的值，但是并不是每一个操作步骤都有值，
        比如sleep操作，这时对应的元素那一列就没有值，所以这里要加一个判断
        '''
        element_key = self.opera_excel.get_cell(row,4)
        if element_key == '':
            return None
        return element_key

    def get_handle_value(self,row):
        '''
        获取操作元素的值，也就是send_keys要输入什么值，获取获取文本等内容

        '''
        handle_value = self.opera_excel.get_cell(row,5)
        if handle_value == '':
            return None

        return handle_value

    def get_expect_element(self,row):
        '''
       获取预期结果元素element

        '''
        except_element = self.opera_excel.get_cell(row,6)

        if except_element == '':
            return None

        return except_element

    def get_is_run(self, row):
        '''
        判断用例是否需要运行，返回True或者False

        '''
        is_run = self.opera_excel.get_cell(row, 8)
        if is_run == 'yes':
            return True
        else:
            return False

    def get_expect_handle(self,row):
        '''
        获取excel中"预期步骤列的值"

        '''
        expect_step = self.opera_excel.get_cell(row,7)
        if expect_step == "":
            return None
        else:
            return expect_step

    def write_value(self,row,value):
        self.opera_excel.write_value(row,value)
