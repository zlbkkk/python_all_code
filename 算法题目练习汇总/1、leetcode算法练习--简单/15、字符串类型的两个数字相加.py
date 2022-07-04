# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
#
#  
#
# 提示：
#
# num1 和num2 的长度都小于 5100
# num1 和num2 都只包含数字 0-9
# num1 和num2 都不包含任何前导零
# 你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式

'''
比如：
    输入：
    "9"
    "99"
    输出：
    "108
'''



def addstring(str1,str2):
    res=""

    i,j,jinwei = len(str1)-1,len(str2)-1,0
    while i>=0 or j>=0:
        n1 = int(str1[i]) if i>=0 else 0  # 把字符串str1的最后一位取出来
        n2 = int(str2[j]) if j>=0 else 0 # # 把字符串str2的最后一位取出来

        tmp = n1 + n2 + jinwei
        jinwei =tmp //10 # 看是否需要进为,如： 9//10=0   18//10=1
        res = str(tmp%10)+res  # res是存储最后结果的，现在根据上面算的 留下最后的那位数，比如不进位：8%10=8  进位：13%10=3
        i,j=i-1,j-1

    return "1"+res if jinwei else res #  "1"+res主要是为了判断最后一位是否大于10，需要进位


print(addstring("98","728"))









def addstr(s1, s2):

    res = ""
    l1, l2, jinwei = len(s1)-1, len(s2)-1, 0
    while l1 > 0 and l2 >0:
        n1 = int(s1[l1]) if l1>=0 else 0
        n2 = int(s2[l2]) if l2>=0 else 0

        sum = n1 + n2 + jinwei
        jinwei = sum // 10
        res = str(sum%10) + res















