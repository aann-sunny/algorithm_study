import sys

input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
dp = [[0] * N for _ in range(N)]

# 길이가 1일때
for i in range(N):
    dp[i][i] = 1

# 길이가 2일때
for i in range(N - 1):
    if lst[i] == lst[i + 1]:
        dp[i][i + 1] = 1

# 길이가 3이상일때
for i in range(2, N):        # 이동한 거리 (길이는 이동한 거리 +1(기준점)이다.)
    for j in range(N - i):   # lst 속 기준점
        # 풀이 아래 참고
        if lst[j] == lst[j + i] and dp[j + 1][j + i - 1] == 1:
            dp[j][i + j] = 1

M = int(input())

for _ in range(M):
    a, b = map(int, input().split())
    print(dp[a - 1][b - 1])

'''
if lst[j] == lst[j + i] and dp[j + 1][j + i - 1] == 1:
양 끝의 값이 같고 양끝에서 한칸씩 안쪽으로 이동한 인덱스의 dp 배열값이 1이면

ex) lst = 3 1 0 1 3 4
기준점 1, 이동한 거리 2 (길이 3)일 때   = 다시 말해 lst[1]~lst[3]
if lst[1]==lst[3] and dp[2][2] == 1:
    dp[1][3] = 1

기준점 0, 이동한 거리 4 (길이 5)일 때   = 다시 말해 lst[0]~lst[4]
if lst[0]==lst[4] and dp[1][3] == 1:
    dp[0][4] = 1

'''
