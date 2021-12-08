# https://www.acmicpc.net/submit/9663
# https://idea-sketch.tistory.com/29
# python은 시간 초과.
# pypy3: 파이썬을 더 빠르게. 지원되지 않는 라이브러리 있음.

import sys


def findAns(n):
    if n == N:  # 마지막 행일 때. N개 만큼 퀸 배치 다 되면.
        global count  # 전역변수 설정했는데 왜 인식 안되는지.
        count += 1
    else:
        for i in range(N):  # 0~N-1
            if visited[i]:
                continue  # if문에 들어오면 반복문 끝으로. -> if-else
            chess_list[n] = i
            flag = False
            for j in range(n):
                if (chess_list[n] == chess_list[j]) or (
                    n - j == abs(chess_list[n] - chess_list[j])
                ):  # 같은 열 또는 대각선 --> 퀸 배치 불가
                    flag = True
            if flag is False:
                visited[i] = True
                findAns(n + 1)  # 다음 행으로.
                visited[i] = False  # 다음 행으로 가니 초기화
                # 재활용 가능


N = int(sys.stdin.readline())

# 2차원 배열 -> 시간 초과
# 인덱스 번호 = 행
# 인덱스 값 = 열

# 0 1 2 3  번호 = 행
# 0 0 0 0  값 = 열
chess_list = [0 for _ in range(N)]
visited = [False for _ in range(N)]

count = 0
findAns(0)
print(count)
