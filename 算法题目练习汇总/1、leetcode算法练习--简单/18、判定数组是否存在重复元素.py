# 给定一个整数数组，判断是否存在重复元素。
#
# 如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。
#
#  
#
# 示例 1:
#
# 输入: [1,2,3,1]
# 输出: true
#




def chongfu(lis):
    if len(lis)==set(lis): #用set去重，判断数组长度是否一致
        return False
    else:
        return True