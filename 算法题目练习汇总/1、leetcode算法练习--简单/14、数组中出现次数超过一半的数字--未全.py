# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
#
#  
#
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
#
#  
#
# 示例:
#
# 输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
# 输出: 2

# 方法1：
a=[1, 2, 5, 5, 5, 2, 5, 4, 2]
import collections
print(collections.Counter(a)) # 结果：Counter({5: 4, 2: 3, 1: 1, 4: 1})

# 思路：一个数组中不可能有两个数出现的次数超过一般以上，只会有一个数
def majorityElement(nums) :
    # collections.Counter(nums).most_common(1)  会返回：[(2, 5)]
    # most_common表示最大的几个
    return collections.Counter(nums).most_common(1)[0][0]


print(majorityElement(a))













from collections import Counter

def max_num(lis):

    return Counter(a).most_common(1)[0][0]







