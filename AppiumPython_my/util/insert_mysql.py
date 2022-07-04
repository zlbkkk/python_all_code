def logging(flag):
    def decorator(func):
        def inner(num1, num2):
            if flag == "+":
                print("--正在努力加法计算--")
            elif flag == "-":
                print("--正在努力减法计算--")
            else:
                print("--正在努力计算不懂法--")
            result = func(num1, num2)
            return result
        return inner
    return decorator

@logging("（")             # @logging("+") ==> @decorator
def add(a, b):
    return a + b

@logging("-")             # @logging("-") ==> @decorator
def sub(a, b):
    return a - b

result = add(1, 2)
print(result)

result = sub(1, 2)
print(result)