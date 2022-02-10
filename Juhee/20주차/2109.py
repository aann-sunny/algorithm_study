# 구현 중

import sys

input = sys.stdin.readline

n = int(input())
univ = []

for _ in range(n):
    pd_list = list(map(int, sys.stdin.readline().split()))
    univ.append(pd_list)

univ.sort(key=lambda x: x[0])
univ.sort(key=lambda x: x[1])

ans = 0
ans += univ[len(univ)-1][0]

for i in range(1, len(univ)):
    if univ[i][1] != univ[i-1][1]:
        ans += univ[i-1][0]

print(ans)
