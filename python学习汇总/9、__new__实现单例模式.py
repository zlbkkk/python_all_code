class Student:

    __isinstance = False # 保存创建好的实例
    def __new__(cls, *args, **kwargs):

        if not cls.__isinstance: # 如果没有创建实例
            cls.__isinstance = object.__new__(cls) # 创建实例

        return cls.__isinstance # 如果有实例，直接返回

    def __init__(self,name):
        print(f"我是{name}")
stu1 = Student("zlb1")
stu2 = Student("zlb2")
print(stu1)
print(stu2)

if hasattr(stu2,"name"):
    print(True)
else:
    print(False)



