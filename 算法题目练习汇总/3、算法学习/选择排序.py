import sys

A = [64, 25, 12, 22, 11,22]
n=len(A)

def select_sort(alist):
    for i in range(n-1):

    # min_dex这个的作用是遍历i右边的元素时，不断的和前面进行比较，找到列表中最小的值，并把这个最小值的索引值保留下来，赋值给min_dex
        min_dex = i
        for j in range(i+1,n): # j从i的右边元素（i的第二个元素）开始取值因为是两两比较，所以从i开始取值就没必要，前面已经取出i等于0了


    # 刚开始从min_dex = i，也就是从第一个元素开始和索引是j相比较，随着遍历，如果前面的大于后面的值，就保留小的值的索引，让min_dex = j
            if alist[min_dex] > alist[j]: #
                min_dex = j # 不断保留小的值的索引值，不断遍历之后，就保留了列表中最小的值

    # 经过上一层的遍历，取到了列表中最小的值，让他和i进行交换，（第一次是第一个值，往后每一次遍历，i就+1，也就是开头已经排好的元素不会在进行交换）
        alist[i],alist[min_dex] = alist[min_dex],alist[i]
    return alist
#
#
#
#
# print ("排序后的数组：",select_sort(A))
# for i in range(len(A)):
#     print("%d" %A[i]),






A = [64, 25, 12, 22, 11,22,1,2,33,0.5]
n=len(A)

def maopao(a):

    for i in range(n):

        min_dex = i

        for j in range(i+1,n):

            if a[min_dex] > a[j]:
                min_dex = j


        a[i],a[min_dex] = a[min_dex],a[i] # 这个交换一定要和这个 for j in range(i+1,n) 平行

    return a

print(maopao(A))








