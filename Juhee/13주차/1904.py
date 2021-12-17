"""
아이디어가 잘 생각나지 않아 예시를 들어 생각
N=4, N=5, N=6 일 때
각각 00이 하나, 00이 둘, ... 일 때를 생각해봄
00이 N//2+1개 일 때가 최대임을 알게 됨.

for문 내 규칙 
-> math.factorial(N - i)) / (math.factorial(i) * math.factorial(N - 2 * i)

시간초과 --> DP 사용해서 다시 해보자
"""

import sys
import math

N = int(sys.stdin.readline())

sum = 0

for i in range(N // 2 + 1):
    sum += (math.factorial(N - i)) / (math.factorial(i) * math.factorial(N - 2 * i))

print(sum % 15746)
