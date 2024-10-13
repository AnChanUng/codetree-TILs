n = int(input())

dp = [0] * 1001

dp[1] = 1
dp[2] = 1
dp[3] = 1
for i in range(4, n+1):
    dp[i] =