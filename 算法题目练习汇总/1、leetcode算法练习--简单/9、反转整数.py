
#方法1：先转成字符串 str

#思路：先转成str，然后判断第一位是否是负号，如果是，从第一位开始取，然后反转

def reverse_int(num):
    s = str(num)

    if s[0] == "-":
        x = int(s[1:][::-1])
    else:
        x = int(s[::-1])

    return x if -2147483648< x <2147483647 else 0  # 2147483647 这个是32位int的表示范围

print(reverse_int(891))


# 方法2：直接使用绝对值的方式：

def reverse(x):
    rev = int(str(abs(x))[::-1])
    return (-rev if x<0 else rev) if rev.bit_length()<32 else 0

print(reverse(891))


#方式3：
# 反转数字  ----有bug，这个如果是负数的时候就会出错
def fanzhuan(num):

    res=0

    while num>0:
        end_num=num%10
        res = res*10+end_num

        num=num//10

    return res

print(fanzhuan(12309))
































