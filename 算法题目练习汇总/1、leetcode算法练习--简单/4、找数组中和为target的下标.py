


# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

nums = [2,7,11,15]
def twoSum(nums, target):
    dic = {}
    for i, n in enumerate(nums):
        if n in dic:
            return [dic[n], i]
        dic[target-n] = i

print(twoSum(nums, 9))