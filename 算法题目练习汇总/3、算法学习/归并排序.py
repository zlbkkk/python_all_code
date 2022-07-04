

def merge_sort(alist):
    n = len(alist)
    mid = n //2

    if n <= 1: # n=1 的时候就不用在继续拆分了
        return alist
        '''
        对上面的这个return alist的解释：
             这个是拆分到不能拆分后，把alist列表返回给递归函数，这个return不会终止函数的执行，
            这个return是执行递归函数时，判断是否还需要递归下去，如果满足条件 if n <= 1，则返回递归函数
            的执行结果，比如：左边函数执行到最后，会把[54]这个列表返回，也就是return [54]
        
        '''

    left_li = merge_sort(alist[:mid])  # 返回归并排序后形成的有序的新列表，因为退出递归的条件是 if n <=1 所以最后left_li的结果是lefi

    right_li = merge_sort(alist[mid:])  # 返回归并排序后形成的有序的新列表,即：步骤4中右边的那个列表 1236

    '''
    注意：left_li = merge_sort(alist[:mid])和right_li = merge_sort(alist[mid:]) 会不断的
    调用自身，进行切割，每调用一次，代码就会从头n = len(alist)往下执行一次，而len(alist)中的alist
    在第一次递归调用时会变成 alist[:mid]，也就是列表长度缩小了一半，直到满足条件if n <= 1，即列表
    长度只剩下一个的时候才会停止递归调用
    
    '''



    left_pointer,right_pointer = 0,0 # 定义两个指针，对应步骤5，分别将左边和右边列表合在一起
    result = []

    '''
        对这个的说明：while left_pointer <len(left_li) and right_pointer < len(right_li): 
        
         当索引left_pointer和right_pointer小于他们列表的长度的时候，不能在继续循环，假如len(left_li)=4
         left_pointer 索引从0开始取值 0 1 2 3 < 4正好取到最后一个值，如果是left_pointer <len(left_li - 1),则取不到最后一个值3
    '''
    while left_pointer <len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] < right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1

    # 退出循环之后，有可能两边列表元素个数不相等，name就会有一边的列表时没有取完的，那就用result这个列表加上左右边列表
    result += left_li[left_pointer:]
    result += right_li[right_pointer:]

    return result # 返回合并好的新列表

if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20,1,0.5]
    print(li)
    sorted_li = merge_sort(li)
    # print(li)
    print(sorted_li)

