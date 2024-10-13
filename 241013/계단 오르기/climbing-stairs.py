n = int(input())

dp = [0] * 1001

for i in range(5, n+1):
    if i <= 4:
        dp[i] = 1
    else:
        dp[i] = dp[i-2] + dp[i-3]

print(dp[n] % 10007)