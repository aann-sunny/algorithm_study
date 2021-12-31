"""
무작정 손으로 적어서 규칙 찾기했으나 답 다름
import sys
import math

N = int(sys.stdin.readline())

dp_list = []
ans = 0
for i in range(0, N):
    ans += math.pow(2, i)

print(ans)
"""
"""
n=0 --> 1
n=1 --> 3
n=2 --> 3+4=7
"""
