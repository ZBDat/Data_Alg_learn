def print_num_recursive(n):
    if n > 0:
        print_num_recursive(n-1)
        print(n)


def print_num_recursive_reverse(n):
    if n > 0:
        print(n)
        print_num_recursive_reverse(n-1)


def hanoi_move(n, source, dest, intermediate):
    if n >= 1:  # 递归出口，只剩一个盘子
        hanoi_move(n-1, source, intermediate, dest)
        print("Move %s -> %s" % (source, dest))
        hanoi_move(n-1, intermediate, dest, source)


def power_sum(a, b, n):
    mod = 1e9 + 7
    if n == 0:
        return 2
    elif n == 1:
        return a
    else:
        dp = [2, a]
        for i in range(2, n+1):
            dp.append((((a * dp[i - 1] % mod) - (b * dp[i - 2] % mod)) + mod) % mod)
        return dp[n]


if __name__ == "__main__":
    """print_num_recursive(5)
    print_num_recursive_reverse(5)
    hanoi_move(3, 'A', 'C', 'B')"""
    nums = [int(x) for x in input().split()]
    a, b, n = nums[0], nums[1], nums[2]
    print(power_sum(a, b, n))
