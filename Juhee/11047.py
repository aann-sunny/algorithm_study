# https://www.acmicpc.net/problem/11047

'''
예시를 통해 "그리디 알고리즘"을 사용할 수 있음을 알 수 있다.
(반례가 없음)

그리디인건 알겠는데 가장 큰 동전을 어떻게 찾지?
동전의 가치는 오름차순으로 주어진다. 이를 이용해보자.
그렇다면 동전의 가치를 담은 리스트의 역순으로 올라가서
만들고자하는 가치의 합 // 동전의 가치를 해서 >= 1 일 때
즉, 내가 만들고자하는 가치의 합을 만들 수 있는 최대 가치의 동전인거를 찾은거지.
그럼 이를 정답 변수에 쌓아주고 만들고자하는 가치의 합에서 총합을 빼주자.

그리디와 DP를 배우고 풀어서 그런지 빠르게 풀 수 있었다.
리스트의 역순을 이용한다는 발상을 생각하는게 포인트인 것 같다.
'''

import sys

input = sys.stdin.readline
N, K = map(int, sys.stdin.readline().split())
value = []
ans = 0

for _ in range(N):
    value.append(int(input()))

for i in range(N):  # 0~9
    count = K//value[N-1-i]
    if count >= 1:
        ans += count
        K -= count * value[N-1-i]

print(ans)
