'''

给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释:连续子数组[4,-1,2,1] 的和最大，为6。

'''

def maxSubArray(nums):
    for i in range(1,len(nums)):
        nums[i] = max(nums[i-1]+nums[i],nums[i]) # 经过相加后,num[i]，已经变成最大的哪一个，然后将num[i]更新到列表中，后面再取num[i]，num[i]其实也就是加好的数

    print(nums)  # 最后，变成：[2, 5, 3, 7, 8, 11]
    return max(nums) # 因为前面相加的值是在列表元素中进行更新，所以现在直接取max即可

nums=[-2,1,-3,4,-1,2,1,-5,4]

print(maxSubArray(nums))







def get_max_num(lis):
    sum = 0

    for i in range(1,len(lis)):
        # lis[i] 将加好的数，放到列表中，最后用max函数就可以求出来
        lis[i] = max(lis[i-1] + lis[i], lis[i-1])
        return max(lis)


print(get_max_num(nums))




















