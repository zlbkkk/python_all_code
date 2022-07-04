

# 1、如果是字符串的话可以这样：
def a(n):

    n=str(n)
    m=n[::-1]
    if(n==m):
        print("yes")
    else:
        print("no")


# 2、将int转化成str类型: 双向队列



# 方法一: 将int转化成str类型: 双向队列
# 复杂度: O(n^2) [每次pop(0)都是O(n)..比较费时]
def isPalindrome(x):
    lst = list(str(x))
    while len(lst) > 1:
        if lst.pop(0) != lst.pop():
            return False
    return True


print(isPalindrome(12345))



# 3、使用数学方法解决


def huiwen(x):
    if x<0 or (x%10==0 and x!=0): # 1:小于0;2:能被10整除（10,100,110,200等）并且不是0;这些都不是回文数
        return False

    reversenum=0
    while x>reversenum:

        '''
        解释1:
         reversenum是构造反过来的数字
         x%10 表示取个位数，如121，取个位数1;reversenum*10，因为后面再加一位就是有十位，
         所以需要乘以10
        '''
        reversenum = reversenum*10+x%10  # 参考解释1
        x=x//10 #经过第一轮后，去掉121中的1，只留下12；最后一轮剩下1,剩1时，此时会跳出循环


    '''
    解释2：  121121
        因为x可能是偶数位数字或者奇数位数字，如果是偶数位数字，则reversenum==x代表回文数;
        如果是奇数位数字，x最后等于1，则中间那个数字不考虑，考虑x==reversenum//10,该题最后为 x=1,reversenum=12,所以 1=12//10
                       比如：2//10=1                    1 ==12//10
        '''
    return reversenum==x or x==reversenum//10 # 参考解释2



print(huiwen(121))

# =============================================

# 反转数字
def fanzhuan(num):

    res=0

    while num>0:
        end_num=num%10
        res = res*10+end_num

        num=num//10

    return res == num

print(fanzhuan(121))


