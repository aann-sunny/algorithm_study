"""
문제 예시를 직접 적어서 해보니 생각보다 아이디어가 빨리 떠오름
서류와 면접 중 하나를 기준으로 sort를 하고(서류를 기준으로 해보자)
바로 밑과 비교하여 밑의 면접 성적보다 낮다면 탈락 높으면 합격
--> 바로 밑은 서류 성적이 더 좋음.
그렇기 때문에 바로 밑보다만 면접 성적이 높으면 되는 줄 알았는데 틀린 답
수정해보기
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

    for i in range(1, N):
        if score_list[i - 1][1] > score_list[i][1]:
            ans += 1
    print(ans)
