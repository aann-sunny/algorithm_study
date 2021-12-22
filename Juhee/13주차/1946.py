"""
문제 예시를 직접 적어서 해보니 생각보다 아이디어가 빨리 떠오름
서류와 면접 중 하나를 기준으로 sort를 하고(서류를 기준으로 해보자)

 바로 위만 영향을 준다고 생각해서 바로 위랑 비교를 하며 풀었으나 틀린 답
 --> 바로 위가 아닌 살아 남은 것 중 하나.(25번째 줄에서 max 이용)

Greedy 알고리즘
"""

import sys

T = int(sys.stdin.readline())

for _ in range(0, T):
    N = int(sys.stdin.readline())
    score_list = [[0 for col in range(2)] for row in range(N)]
    ans = 1  # 밑에서 sort하므로 맨 마지막은 무조건 ans에 추가. 미리 +1
    for i in range(0, N):
        score1, score2 = map(int, sys.stdin.readline().split())
        score_list[i][0] = score1
        score_list[i][1] = score2
    score_list.sort(key=lambda x: x[0])

    max = score_list[0][1]  # max 변수를 통해 for문 하나 줄여 시간 단축
    for i in range(1, N):
        if max > score_list[i][1]:
            max = score_list[i][1]
            ans += 1

    print(ans)
