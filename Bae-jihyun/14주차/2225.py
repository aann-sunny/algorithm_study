'''
접근 1 : 완전 탐색
for i in range(N+1)인 for문이 k개가 필요하기 때문에 O(n^k)이다.
최대 N:200, k:200이기 때문에 200^200으로 시간초과.(실패)

접근 2 : DP
문제를 보고 바로 DP로 풀 수 있을거라는 감이 왔다.
dp 문제를 풀 때처럼 변수가 될 N과 K를 각각 행렬로 두고 2차원 배열을 만들어 결과값으로 표를 채웠다.
금방 점화식을 찾을 수 있었다!

N\K | 1 2 3 4 5 6
1     1 2 3 4 5 6
2     1 3 6 1O
3     1 4 10
4

점화식 : dp[i][j] = dp[i-1][j] + dp[i][j-1]
'''
N, K = map(int, input().split())
dp = [[1]*K for _ in range(N)]

for i in range(1, K):
    dp[0][i] = i+1

for i in range(1, N):
    for j in range(1, K):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000000

print(dp[N-1][K-1])

'''
%(모듈러)연산은 매번(27번째 줄에서) 해주는 것이 좋음
'''
