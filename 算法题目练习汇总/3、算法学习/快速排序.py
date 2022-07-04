'''
    排序的思想：
    排序算法的思想非常简单，在待排序的数列中，我们首先要找一个数字作为基准数（这只是个专用名词）。为了方便，
    我们一般选择第 1 个数字作为基准数（其实选择第几个并没有关系）。接下来我们需要把这个待排序的数列中小于
    基准数的元素移动到待排序的数列的左边，把大于基准数的元素移动到待排序的数列的右边。这时，
    左右两个分区的元素就相对有序了；接着把两个分区的元素分别按照上面两种方法继续对每个分区找出基准数，
    然后移动，直到各个分区只有一个数时为止。

'''


def quick_sort(alist, first, last):
    if first >= last:  # 加上尾部递归的终止条件,这里必须要大于等于，只等于==会报错
        return

    mid_value = alist[first]
    low = first
    high = last

    while low < high:  # 有个大的循环条件包着，刚开始只要low和high没有重合就可以进入

        '''
        对下面的说明：
        一、while low < high and alist[high] > mid_value: 
            让右边的high先走：
            1、 low < high 是指两个指针还没有相遇的时候，也就是没把mid_value找出来的时候
            2、alist[high] >= mid_value 时，让high继续往左走
            3、当这两个条件都不满足的时候，把high的值放到low位置处，即：low位置等于high位置的值
                此时因为先让high移动，low还在第一位

        二、对这个的说明：while low < high and alist[high] >= mid_value
            1、  这里的low < high不能省略，因为有可能进入第一层while之后，经过遍历，是有可能low和high相等的

        三、alist[high] >= mid_value，为什么要有等于?
            把等于mid_value的固定放在mid_value的一侧，如果没有等于，左边指针遍历到就会往右边移动，右边遍历到就会往左边
            移动，这样就会乱，固定的话就是全部放在右边

        '''
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]  # 交换位置，如果high指到的值小于mid_value，就让high的值移到low的位置

        ##上面交换完位置后，开始让low指针移动，这个是第一次写法
        # low += 1
        '''
        关于上面 low += 1的说明：
        # 不能这样写，因为当上面的high移动的过程中都，值都大于等于54，那high就会与low重合,此时退出上面high -=1的whiile循环，
        但是low += 1是在while循环体外，就会接下来执行 low += 1 此时low和high已重合，但现在low又往前移动一位，就会错过，
        也就会产生问题

        '''

        while low < high and alist[low] < mid_value:
            low += 1  # 确保low指针的移动是在和high没有重合的情况下才移动

        alist[high] = alist[low]  # 交换位置，如果low指到的值大于mid_value，就让low的值移到high的位置

        # 上面交换完位置后，开始让high指针移动
        # high -= 1 # 这样写有问题，和上面的low +=1 原理一样，

    # alist[low] = mid_value  和下面那个alist[high] = mid_value 写法是一样的

    alist[high] = mid_value  # 经过遍历，low = high时，退出循环，也就是知道了mid_value这个中间值该放哪个位置

    '''
        以下内容是递归:
    此时还需要递归重复以上步骤进行排序，直到拿出中间元素后，左右两边的序列只剩一个才停止

    '''

    quick_sort(alist, 0, low - 1)  # mid_value左边的序列
    quick_sort(alist, low + 1, last)  # 调用是 last = len(alist)-1 ,因为列表索引是从0开始， 然后len(alist)-1 刚好是最后一个值的索引


if __name__ == "__main__":
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20, 1]
    print("排序前：", alist)
    quick_sort(alist, 0, len(alist) - 1)
    print("排序后:", alist)



















