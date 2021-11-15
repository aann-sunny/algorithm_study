#1149
# H(i) != H(i-1) != H(i+1)
import sys

N = int(sys.stdin.readline())
cost = []

for _ in range(N):
    cost.append(list(map(int, input().split())))

dp = [[10000011] * 3 for _ in range(N)]  # R=0 G=1 B=2
dp[0][0] = cost[0][0]
dp[0][1] = cost[0][1]
dp[0][2] = cost[0][2]

for i in range(1, N):
    dp[i][0] = cost[i][0] + min(dp[i - 1][1], dp[i - 1][2])
    dp[i][1] = cost[i][1] + min(dp[i - 1][0], dp[i - 1][2])
    dp[i][2] = cost[i][2] + min(dp[i - 1][0], dp[i - 1][1])

print(min(dp[N - 1]))