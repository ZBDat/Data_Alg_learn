def quick_sort(list):
    # 不基于交换的快排，需要额外空间
    if len(list) <= 1:
        return list
    else:
        pivot = list[0]
        smaller = []
        larger = []
        for i in range(1, len(list)):
            if list[i] <= pivot:
                smaller.append(list[i])
            else:
                larger.append(list[i])
        list1 = quick_sort(smaller)
        list2 = quick_sort(larger)
        return list1 + [pivot] + list2


def partition(array, beg, end):
    # 双指针从两侧遍历，目标情况下，l的指针走过的位置应该比pivot小， r指针则大
    # 所以先交换不满足的l和r元素，满足的话就移动指针到下个位置
    # r所停的最后位置是最后一个比pivot小的（因为是l刚越过的位置），交换它和pivot即可
    pivot_index = beg
    pivot = array[pivot_index]
    left = pivot_index + 1
    right = end   # 开区间，最后一个元素位置是 end-1     [0, end-1] or [0: end)，括号表示开区间

    while True:
        # 从左边找到比 pivot 大的
        while left <= right and array[left] < pivot:
            left += 1

        while right >= left and array[right] >= pivot:
            right -= 1

        if left > right:
            break
        else:
            array[left], array[right] = array[right], array[left]

    array[pivot_index], array[right] = array[right], array[pivot_index]
    return right   # 新的 pivot 位置


def quicksort_inplace(array, beg, end):    # 注意这里我们都用左闭右开区间，end 传入 len(array)
    # no need for extra storage
    if beg < end:    # beg == end 的时候递归出口
        pivot = partition(array, beg, end)
        quicksort_inplace(array, beg, pivot)
        quicksort_inplace(array, pivot+1, end)


if __name__ == "__main__":
    array = [2, 0, 3, 1, -5, -1]
    quicksort_inplace(array, 0, len(array)-1)
    print(array)
