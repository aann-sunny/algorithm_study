"""
이게 어떻게 정답률 41프로지
어려웠던 문제

예를 들어 생각해보자.
n=10, k=3라면
1. 0+ 10을 3개로 나눈 것
2. 1+ 9을 3개로 나눈 것
...
3. 9+ 1을 3개로 나눈 것
4. 10+ 0을 3개로 나눈 것

표를 적어서 생각해보자.

K/N  1  2  3  4
 1   1  1  1  1
 2   2  3  4  5
 3   3  6  10 15

무작정 규칙찾기로 품
--> dp_list[i][j] = dp_list[i - 1][j] + dp_list[i][j - 1]
"""

import sys

N, K = map(int, sys.stdin.readline().split())

dp_list = [[0] * (K + 1) for _ in range(N + 1)]
dp_list[0][0] = 1

for i in range(0, N + 1):  # 0~N
    for j in range(1, K + 1):  # 1~K
        dp_list[i][j] = dp_list[i - 1][j] + dp_list[i][j - 1]

print(dp_list[N][K] % 1000000000)
