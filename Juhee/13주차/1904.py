"""
아이디어가 잘 생각나지 않아 예시를 들어 생각
N=4, N=5, N=6 일 때
각각 00이 하나, 00이 둘, ... 일 때를 생각해봄
00이 N//2+1개 일 때가 최대임을 알게 됨.

for문 내 규칙
-> math.factorial(N - i)) / (math.factorial(i) * math.factorial(N - 2 * i)

시간초과
N이 최대 100만 -> 타일 100만
최대 2^100만 -> 불가능
(N이 최대 10,000,000인 경우 O(N) 가능)
--> DP 사용해서 다시 해보자

00의 개수로 경우의 수를 나누지 말고 개수를 세보니 규칙 나옴
핵심: 전의 것을 이용하자.

등수 헷갈리면: -붙여보기
ex 1등, 5등 -> =1 -5 점수 -1이 더 높음
"""

import sys

N = int(sys.stdin.readline())

dp_list = [0] * 1000001
dp_list[1] = 1
dp_list[2] = 2

for i in range(3, N + 1):
    dp_list[i] = (dp_list[i - 1] + dp_list[i - 2]) % 15746

print(dp_list[N])
