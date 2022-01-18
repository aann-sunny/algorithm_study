"""
1. 각각 리스트에 담고 이중 for문 돌리기
--> 10^4 * 10^4 = 10^8 시간초과
2. list in
--> 이중 for문보다 시간이 더 적게 걸리나보다
"""

import sys

input = sys.stdin.readline
N, M = map(int, input().split())

s_list = []
test_list = []

for _ in range(N):
    s_list.append(input())
for _ in range(M):
    test_list.append(input())

ans = 0


for j in range(len(test_list)):
    if test_list[j] in s_list:
        ans += 1

print(ans)
