"""
규칙 찾기했으나 답 다름
import sys
import math

N = int(sys.stdin.readline())

dp_list = []
ans = 0
for i in range(0, N):
    ans += math.pow(2, i)

print(ans)
"""

n = int(input())
s = [[0] * 3 for i in range(100001)]
for i in range(3):
    s[1][i] = 1
# s[n][0]: 맨 위의 두 칸 중 사자가 왼쪽
# s[n][1]: 맨 위의 두 칸 중 사자가 왼쪽
# s[n][2]: 맨 위의 두 칸 중 사자가 왼쪽
for i in range(2, 100001):
    s[i][0] = s[i - 1][1] + s[i - 1][2] % 9901  # 메모리 초과
    s[i][1] = s[i - 1][0] + s[i - 1][2] % 9901
    s[i][2] = s[i - 1][0] + s[i - 1][1] + s[i - 1][2] % 9901
print(sum(s[n]) % 9901)
