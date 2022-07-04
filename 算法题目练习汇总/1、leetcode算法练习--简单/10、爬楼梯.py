
'''
示例1：
    输入： 2
    输出： 2
    解释： 有两种方法可以爬到楼顶。
    1.  1 阶 + 1 阶
    2.  2 阶

示例2：

    输入： 3
    输出： 3
    解释： 有三种方法可以爬到楼顶。
    1.  1 阶 + 1 阶 + 1 阶
    2.  1 阶 + 2 阶
    3.  2 阶 + 1 阶


'''
#规律： 通过上面可以发现，第三个数是前面两个数相加之和

def pa(n):

    dic={}
    dic[1]=1
    dic[2]=2
    for i in range(3,n+1):
        dic[i] = dic[i-1]+dic[i-2]  # i前面的两个数相加之和
    return dic[n]

print(pa(5))



def pa1(n):
    d = {}
    d[1]=1
    d[2]=2
    for i in range(3,n+1):
        d[i] = d[i-1] + d[i-2]
    return d[n]

print(pa1(1))