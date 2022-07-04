'''
    给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

    不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

    示例 1:

    给定数组 nums = [1,1,2],

    函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。

    你不需要考虑数组中超出新长度后面的元素。

'''



def remove(lis):
    # 说明：
    #     i负责指向不含重复元素序列的最后一个元素
    #     j负责指向未进行决策的序列的首个元素

    i=0
    if len(lis)==0:
        return 0
    for j in range(len(lis)):
        if lis[j] != lis[i]:
            i += 1 # 负责计算数组的长度

        # 这行代码意思是：比如[1,1,2]，他会把2向前移，让从头开始过来的数组没有重复的元素，为：[1,2,1]

            lis[i],lis[j] = lis[j],lis[i]

    print(lis)
    return i+1

nums = [1,1,2,2,3,4,5]

print(remove(nums))




# def return_legth(lis):
#     i,j=0,0
#
#     for _ in range(len(lis)):
#         if lis[j] != lis[i]:
#             i+=1
#             lis[i],lis[j]=lis[j],lis[i]
#
#         j+=1
#
#     return i+1
#
# nums = [1,1,2,2,3,4,5]
# print(return_legth(nums))



