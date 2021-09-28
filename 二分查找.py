def binary_search1(list, x, l, r):
    """
    :param list: the candidate list
    :param l: left most index
    :param r: right most index
    :param x: the target
    :return: the index of the target. -1 if no in the list
    """
    # 递归版本
    # 递归版本均需要左右下标
    if l > r:
        return -1
    else:
        mid = l + (r - l) // 2
        if list[mid] == x:
            return mid
        elif list[mid] > x:
            return binary_search1(list, x, l, mid-1)
        elif list[mid] < x:
            return binary_search1(list, x, mid+1, r)


def binary_search2(list, x):
    # 循环版本
    l = 0
    r = len(list) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if list[mid] == x:
            return mid
        elif list[mid] < x:
            l = mid + 1
        elif list[mid] > x:
            r = mid - 1
    return -1


def isBadVersion(n):
    if n >= 4:
        return True
    else:
        return False


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 0
        r = n - 1
        while l < r:
            mid = l + (r - l) // 2
            if isBadVersion(mid):
                r = mid - 1
            else:
                l = mid + 1
        return mid


def insert_pos(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
    return l



if __name__ == "__main__":
    list = [1, 2, 3, 5, 1, 0, -2, -5]
    list.sort()
    print(list)
    print(binary_search1(list, 0, 0, len(list)-1))
    print(binary_search2(list, 0))
    print(insert_pos(list, 4))
