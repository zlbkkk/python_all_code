


# def binary_search(alist,find_num):
#     n = len(alist)
#
#
#     if n > 0:  # 当n = 0时代表找不到
#         mid_num = n // 2
#         if find_num == alist[mid_num]:
#             return "找到了"
#
#
#
#         elif find_num < alist[mid_num]:
#             alist= alist[:mid_num]
#             return binary_search(alist,find_num)
#
#         else:
#             return binary_search(alist[mid_num+1:],find_num)
#
#     return "元素不在列表中"


def binary_search(alist, item):
    """二分查找,递归"""
    n = len(alist)
    mid = n // 2
    if n > 0:

        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binary_search(alist[:mid], item)
        else:
            return binary_search(alist[mid+1:], item)
    return False




def bin_search(alist,find_num):
    n = len(alist)
    first = 0
    last = n-1

    while first == last:
        mid_num = (first + last) // 2
        if find_num == alist[mid_num]:
            return "找到了"
        elif find_num < alist[mid_num]:
            last = mid_num - 1
        else:
            first = mid_num +1

    return "找不到"










if __name__ == "__main__":
    lis = [1,3,22,33,44,55,66,77,88,99,100]

    print(binary_search(lis,88))

    print(1/3)