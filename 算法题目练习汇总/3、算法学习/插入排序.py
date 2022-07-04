# def insert_sort(alist):
#     # 从第二个位置，即下标为1的元素开始向前插入
#     for i in range(1, len(alist)):
#         # 从第i个元素开始向前比较，如果小于前一个元素，交换位置
#         for j in range(i, 0, -1):
#             if alist[j] < alist[j-1]:
#                 alist[j], alist[j-1] = alist[j-1], alist[j]
#
# alist = [54,26,93,17,77,31,44,55,20]
# insert_sort(alist)
# print(alist)

def insert_sort(lis):
    n = len(lis)

    for i in range(1,n): #从第2个元素开始，与第一个元素进行比较，n不会被取到，也就是循环次数等于数量长度减1次，原因是第一个元素不用比较了

        for j in range(i,0,-1): # j不断递增，1 2 3 4

            if lis[j] < lis[j-1]:
                # lis[j],lis[j-1] = lis[j-1],lis[j]
                lis[j - 1],lis[j] = lis[j],lis[j-1]

    return lis # 这个return必须在这里，要不然执行了一次循环之后碰到return程序就不会进行新的一次循环了







if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20,1,0.5]
    print("原列表为：%s" % alist)
    insert_sort(alist)
    print("新列表为：%s" % alist)