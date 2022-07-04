#创建类
class main:
    a = 1
    b = 2

    def run(self):
        print(123)

#实例化类
o = main()
o1 = main()

#新增属性C
setattr(o, 'c', 5)

#打印新输出
print(o.c)
print(o1.c)