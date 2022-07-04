# 给定一个字符串，请你找出其中不含有重复字符的最长子串的长度。
#
#     示例:
#
#     输入: "abcaefgu"
#     输出: 3
#     解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。


def zichuan(s):

    s1="" # for循环遍历，把不存在与s2的字串放到s1中
    s2=""  #如果len(s1)>len(s2) ,则让s2等于s1字串，用s2保存s1的字符串
    for i in s:
        if i not in s2:
            s2 += i
        else:
            s2 = s2[s2.index(i)+1:] # （意思是把s2清空）走到这里，代表i是重复的,所以把前面已经添加到s2的字符串都去掉，从i的后一位开始要
            s2 += i  # s2存储不重复的字符串重新 + i

        if len(s2)>len(s1):   # s1的作用是把s2存储下来的不重复的字串存起来，存储s2最大的那个数值
            s1=s2 # 使用新的变量s2，把已经过滤出来的不重复的字符保存起来

    return len(s2)  # 如果新加的字串s1不大于s2，那说明新加的连续的字串还是s2最大

print(zichuan("abc aefgu"))
a=""
print("==========")
print(a[2:])



















def zichuan(s):
    s1 = ""
    s2 = ""

    for i in s:
        if i not in s2:
            s2 += i

        else:
            s2 = s2[s2.index(i)+1:]
            s2 += i

        if len(s2) > len(s1):
            s1 = s2

    return len(s1)











