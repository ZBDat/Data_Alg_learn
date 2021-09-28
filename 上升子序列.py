def ascending_subseq(nums, k):
    # find the number of ascending subsequence of length k.
    n = len(nums)
    dp = [[0] * n for _ in range(k)]
    for i in range(n):
        dp[0][i] = 1
    
    # building up the matrix dp[][]
    # increassing subsequence of size (l+1).
    for l in range(1, k):
 
        # for each increasing subsequence of
        # size 'l' ending with element nums[i]
        for i in range(l, n):
 
            # count of increasing subsequences of
            # size 'l' ending with element nums[i]
            dp[l][i] = 0
            for j in range(l-1, i):
                if (nums[j] < nums[i]):
                    dp[l][i] += dp[l - 1][j]
             
    # Sum up the count of increasing subsequences
    # of size 'k' ending at each element nums[i]
    sum = 0
    for i in range(k-1, n):
        sum += dp[k-1][i]
 
    # required number of increasing
    # subsequences of size k
    return sum


if __name__ == "__main__":
    k = int(input())
    nums = list(map(int, input().split()))
    res = ascending_subseq(nums, k)
    print(res)
