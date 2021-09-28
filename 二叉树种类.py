# 限制高度的情形。在卡特兰数基础上增加一维度
MOD = 10**9+7
n, m = input().split()
n, m = int(n), int(m)
dp = [[0] * (n+1) for _ in range(m+1)]
for j in range(1, m+1):
    dp[j][0] = 1
    dp[j][1] = 1
for i in range(2, n+1):
    for j in range(2, m+1):
        for k in range(i):
            dp[j][i] += dp[j-1][i-1-k]*dp[j-1][k]

print(dp[-1][-1] % MOD)
