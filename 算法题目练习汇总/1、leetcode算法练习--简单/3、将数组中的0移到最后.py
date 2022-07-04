# 1、nums中0不连续的情况：
'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
'''

nums = [1, 2, 0, 1, 0, 3, 12]

z = 0
for i in range(len(nums)):

    # 2、如果nums[i]等于0，就不会往下执行，那么z就不会加1，
    #    直接跳到for i循环，此时i+1，就会比z大1，此时下面就是相互交换
    if nums[i] != 0:
        # 1、不等于0时，i和z是一样的，就不需要替换
        nums[z], nums[i] = nums[i], nums[z]

        z += 1

print(nums)






























def yidong(lis):
    index = 0

    for i in range(len(lis)):

        if lis[i] != 0:
            lis[index], lis[i] = lis[i], lis[index]
            index += 1

    return lis



nums = [1, 2, 0, 1, 0, 3, 12]

print(yidong(nums))



