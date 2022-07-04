#整个关键字模型程序的入口
from keywords.get_data import GetData
from keywords.action_method import ActionMethod
from util.server import Server



class RunMain:

    def run_main(self):
        server = Server()
        data = GetData() #封装了从excel中获取单元格数据
        action_method = ActionMethod()  #封装了关键字
        lines = data.get_case_lines()
        for i in range(1,lines): #1代表着第一行是标题我们不需要
            handle_step = data.get_handle_step(i)  #先获取操作步骤,excel的值对应的是ActionMethod类中函数的名字
            element_key = data.get_element_key(i)  #获取操作元素的key,也就是元素的定位信息
            handle_value = data.get_handle_value(i) #要对元素输入什么值
            expect_key = data.get_expect_element(i) #excel中的预期结果，只是一个键值，
            expect_step = data.get_expect_handle(i) #,获取excel中“预期步骤”列的值，excel的值对应的是ActionMethod类中函数的名字
            '''
            对这句代码的说明：excute_methor = getattr(action_method,handle_step)
                handle_step是获取excel中的“步骤”列的值，该值写的是action_method.py中我们封装的类ActionMethod中函数的名称，
                找到该函数名称后，通过getattr去执行该函数，
            
            '''
            excute_methor = getattr(action_method,handle_step)

            if element_key != None: #在excel中，元素有可能为空，比如sleep()，所以先判断一下
                excute_methor(element_key,handle_value) #比如这个是对ActionMethod类中input函数的操作，element_key,handle_value是input函数的参数
            else:
                excute_methor(handle_value)


            if expect_step != None:  #判断excel预期步骤是否有值

                # 下面的代码含义：expect_step是一个函数的名称，在ActionMethod()类中，比如get_element()函数
                expect_result = getattr(action_method,expect_step)

    # 下面的代码含义：向函数中传入expect_key参数,一个键值，比如username，也就是通过get_element()函数，传入键为username，去获得username这个输入框的定位信息
                result = expect_result(expect_key)
                if result:
                    data.write_value(i,"pass")
                else:
                    data.write_value(i,"fail")















if __name__ =="__main__":
    # a=RunMain()
    #
    # a.run_main()

    run = RunMain()
    run.run_method()






'''
Python中getattr用法:

使用背景：你有一个字符串形式的方法名称，想通过它调用某个对象的对应方法。

1、含义、介绍：
    getattr() 函数用于返回一个对象属性值,
    第一个参数是对象实例obj,name是个字符串，是对象的成员函数名字或者成员变量，
    default当对象没有这个属相的时候就返回默认值，如果没有提供默认值就返回异常。

2、例子1：
    >>> class A(object):        
    ...     def set(self, a, b):
    ...         x = a        
    ...         a = b        
    ...         b = x        
    ...         print a, b   
    ... 
    >>> a = A()                 
    >>> c = getattr(a, 'set')
    >>> c(a='1', b='2')
    2 1

3、例子2
    >class A(object):
        ...     bar = 1
        ... 
        >>> a = A()
        >>> getattr(a, 'bar')        # 获取属性 bar 值
        1
    

4、例子4：
    >>> class Test(object):
    ...     def func(self):
    ...             print 'I am a test'
    ...
    >>> test = Test()  # 实例化一个对象
    >>> func = getattr(test, 'func') # 使用getattr函数获取func的值
    >>> func()
    I am a test








'''