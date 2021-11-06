"""
무식하게 풀기 : 각 테스트별로 2차원으로 주어진 필드의 각 지점을 순회하며 섬의 개수를 세기
가로 세로의 최대는 49인데 약 50으로 뭉탱이쳐서 계산하면 2500번만 계산하면 됨.
계산방법 : 안전영역 때처럼 인접한 지역들 재귀로 방문처리하기.
단 방향을 상하좌우 뿐만 아니라 대각선 방향도 해주기

"""

import sys
sys.setrecursionlimit(10000)
data = []

# 인접한 섬들 방문처리(다 같은 섬에 속한다고 처리 -> 0으로 바꿔서)
def check(w, h, r, c):
    data[r][c] = 0
    directions = [(r - 1, c), (r - 1, c + 1), (r, c + 1), (r + 1, c + 1), (r + 1, c), (r + 1, c - 1), (r, c - 1), (r - 1, c - 1)]
    for nr, nc in directions:
        if (0 <= nr < h) and (0 <= nc < w) and data[nr][nc]:
            check(w, h, nr, nc)


# 섬들의 개수 구해서 리턴
def solution(w, h):
    answer = 0
    for r in range(h):
        for c in range(w):
            if data[r][c]:
                answer += 1
                check(w, h, r, c)
    return answer


while(True):
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break

    for _ in range(h):
        data.append(list(map(int, sys.stdin.readline().split())))
    
    print(solution(w, h))
    # data초기화
    data.clear()