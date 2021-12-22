"""
처음에 문제 보고 생각 한 것은 로프 최대 중량 중 가장 작은 것 * N 아닌가
임의로 몇 개 로프 고르기 가능이 변수

가장 먼저 예시를 들어서 생각해보자
ex N=5일 때 5 10 20 25 30
1.5*5=25
2.10*4=40
3.20*3=60
4.25*2=50
5.30*2=60
처음 생각한 것과는 역시나 다르게 5*5가 가장 크지 X

예시를 보고 생각난 아이디어:
sort를 하고 for문을 돌려 무게와 i 역순으로 해서 곱한 것 중 최대를 뽑자!

한번에 혼자 힘으로 풀어서 뿌듯했던 문제
"""

import sys

N = int(sys.stdin.readline())
rope_list = []

for _ in range(0, N):
    w = int(sys.stdin.readline())
    rope_list.append(w)

rope_list.sort()
max = rope_list[0] * N

for i in range(1, N):
    if max < rope_list[i] * (N - i):
        max = rope_list[i] * (N - i)

print(max)
