import copy


def combine(n, k):
    nums = [i for i in range(1, n+1)]
    res = []

    def backTrace(start, tmpNums):
        if len(tmpNums) == k:
            res.append(tmpNums[:])
            return

        for i in range(start, n):
            tmpNums.append(nums[i])
            backTrace(i+1, tmpNums)
            tmpNums.pop()

    if n == 0 or k == 0 or k > n:
        return

    if k == n:
        return [nums]

    backTrace(0, [])

    return res


def subsets(nums):
    result = []
    temp = []

    def backtrack(nums, startIndex):

        length = len(nums)
        global temp
        result.append(copy.deepcopy(temp))  # 收集所有节点
        if startIndex >= length:
            return

        for i in range(startIndex, length):  # startIndex决定遍历宽度，有序
            temp.append(nums[i])
            backtrack(nums, i + 1)  # i决定遍历深度，i+1表示无重复
            temp = temp[:-1]

    del result[:]
    del temp[:]

    if nums == []:
        return result
    else:
        backtrack(nums, 0)
        return result


if __name__ == "__main__":
    n, k = 4, 3
    res = combine(n, k)
    print(res)
