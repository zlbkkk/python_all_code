
'''
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

'''

# 无注释版：

def three_sum(alist):
    if not alist or len(alist) < 3:
        return "数组个数小于3或数组为空"
    alist.sort()
    n = len(alist)
    res = []  # 存放三个元素加起来为0的三个元素
    
    for i in range(n):
        if alist[i] > 0:
            return res  # 排序后的数组，第1个元素都大于0 ，那相加不会大于0
        if (i > 0 and alist[i] == alist[i - 1]):  # 参考解释2
            continue
        L = i + 1
        R = n - 1

        while L < R:  # 当L和R还没有重逢的时候
            if (alist[i] + alist[L] + alist[R]) == 0:

                res.append([alist[i], alist[L], alist[R]])

                while (L < R and alist[L] == alist[L + 1]):  # 参照 ：解释1
                    L = L + 1
                while (L < R and alist[R] == alist[R - 1]):  # 参照 ：同理参照：解释1
                    R = R - 1

                L = L + 1
                R = R - 1
            elif (alist[i] + alist[L] + alist[R] > 0):  # 若和大于 0，说明 nums[R]太大，R要左移
                R = R - 1

            else:  # 这个是 (alist[i]+alist[L]+alist[R] < 0)的时候，L要向右移
                L = L + 1

    return res


a = [-1, -1, -3, 3, 4, 5, 6, 6, 7, 0]
print(three_sum(a))