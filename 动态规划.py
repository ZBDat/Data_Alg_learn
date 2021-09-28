from typing import List


# 爬楼梯
def climbStairs(n: int) -> int:
    # 观察发现是斐波那契数列
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return climbStairs(n - 1) + climbStairs(n - 2)


# 连续子数组和
def subArray(nums: List[int]) -> int:
    pre = 0
    maxSum = nums[0]
    for i in range(len(nums)):
        pre = max(pre + nums[i], nums[i])
        maxSum = max(maxSum, pre)
    return maxSum


if __name__ == "__main__":
    res = subArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print(res)
