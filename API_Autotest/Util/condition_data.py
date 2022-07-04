#此py文件主要是处理excel中用例依赖的

import os
import json
base_path = os.path.dirname(os.getcwd())
from Util.handle_excel import HandExcel
from jsonpath_rw import parse

excel_data = HandExcel()

def split_data(data):
    '''
        根据>拆分，获取用例编号和匹配规则
        # excel中是这样写的：传进data 的值，data的值为 imooc_001>data.banner.[0].id
    '''

    case_id = data.split(">")[0] # 获取用例编号 case_id
    rule_data = data.split(">")[1] # 得到 data.banner.[0].id
    return case_id,rule_data


def depend_data(data):
    '''
    获取被依赖用例的“结果报文”单元格的值：
    函数作用：传入data，值为：imooc_001>data.banner.[0].id，
    根据获取到的被依赖case所在的行号，还有固定的列号，获取被依赖case的存储返回结果单元格的值

    '''
    case_id = split_data(data)[0] # 拿imooc_001>data.banner.[0].id去切割，获取到的是imooc_001
    row_number = excel_data.get_rows_number(case_id) #获取到被依赖case的行号
    data = excel_data.get_cell_value(row_number,14) # 获取被依赖case执行结果，即：存放结果报文的单元格
    return data


def get_depend_data(res_data,key):
    '''
    获取依赖字段的值：
    比如依赖case1中id字段的值，内容为：  id：1709，则该函数获取到的值为1709
    :key 是一个取值的规则，如：data.banner.[0].id
    :res_data 代表返回的结果报文，在这个报文中根据这个规则data.banner.[0].id去查找匹配的值

    jsonpath_rw的parse用法参考：有道笔记的第四条：
    http://note.youdao.com/noteshare?id=78640593d35fae73eb9a22e8a178ef14&sub=6C2C4CDCB9D1456AB9C2DDDE38F61EC7

    '''
    '''
        解释1：
        # 这个要转换为字典格式，要不然下面json_exe.find(res_data)会找到的是一个空列表[] 
        进而引发[math.value for math in madle][0]会报 IndexError: list index out of range
        
    '''
    res_data = json.loads(res_data) # 解释1
    json_exe = parse(key)
    madle = json_exe.find(res_data)  # find后面的res_data类型要是字典格式  参考解释1
    print("------->madle的值是：",madle)
    return [math.value for math in madle][0] # 后面的这个[0]，因为返回的是一个list，但是我们需要的是一个值，所以这样[0]就可以提取出来单个值



def get_data(data):
    '''
    函数作用：获取字段的值
    这个方法实际上把上面那三种总结在一起，方便调用而已
    data的值为，如：imooc_001>data.banner.[0].id

    '''
    res_data = depend_data(data) # res_data = 依赖用例“结构报文单元格”的值
    rule_data = split_data(data)[1]  # rule_data = data.banner.[0].id
    return get_depend_data(res_data,rule_data) # 返回的是依赖的值，就是那个id字段的值 1709




# if __name__=="__main__":
#     print(depend_data("  imooc_001>data.banner.[0].id"))
#     print(get_depend_data())