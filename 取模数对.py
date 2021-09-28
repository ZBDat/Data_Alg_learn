t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    nums = list(range(1, n+1))
    if k > nums[-1]:
        print(0)
    if k == 0:
        ans = n - k - 1
        for i in range(1, n//2):
            ans += nums[-1] // nums[i] - 1
    else:
        ans = n - k
        for i in range(k, n):
            fold = nums[-1] // nums[i]
            left = nums[-1] % nums[i]
            if left < k:
                ans += fold - 1
            if left == k:
                ans += fold
    print(ans)