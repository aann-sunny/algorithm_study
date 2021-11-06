"""
무식하게 풀기 : 0 ~ 100까지 비의 양을 다르게 하며 하나하나 세보기
N * N 꼴로 주어지는 필드를 하나하나 순회하며 영역개수를 센다고 할 때
이론상 비의 양 최대 100, N의 최대 = 100이므로
100 * 100 * 100 = 1,000,000번 정도의 계산을 하게 될 것 같은데
제한시간은 1초고 파이썬은 대략 5천만번의 연산을 1초내에 할 수 있으므로?
주어진 시간 내에 통과할 수 있을 듯 하다.

이 때 비의 양이 필드에서의 높이의 최댓값과 같아진다면 그 때부턴 비의 양을 늘려도 
전부 다 물에 잠기므로, 비의 양을 100까지 순회하는게 아니라 필드에서의 높이의 최대까지만 
순회하면 될 것  같다.

또한 비의 양이 0일 때 안전영역은 1이 되므로(각 지점의 최소 높이가 1이여서)
정답이 될 수 있는 값의 디폴트는 1로 설정하고 비의 양을 0부터가 아닌 1부터 순회하는 식으로 했다.
"""

import sys
sys.setrecursionlimit(10000)

N = int(sys.stdin.readline())
height, checked = [], []

for _ in range(N):
    height.append(list(map(int, sys.stdin.readline().split())))
    checked.append([True] * N)

# 인접한 영역들 싹 다 표시하기
def checkArea(N, r, c):
    checked[r][c] = False
    directions = [(r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)]
    for nr, nc in directions:
        if (0 <= nr < N) and (0 <= nc < N) and checked[nr][nc]:
            checkArea(N, nr, nc)  


# 빗물의 높이가 rain으로 주어졌을 때 안전영역 개수 계산
def calculate(N, rain):
    areas = 0
    # 잠기는 영역들 구하기 - False로 표현
    for r in range(N):
        for c in range(N):
            if rain >= height[r][c]:
                checked[r][c] = False
            else:
                checked[r][c] = True
    # 안전 영역 개수 구하기
    for r in range(N):
        for c in range(N):
            if checked[r][c]:
                checkArea(N, r, c)
                areas += 1
    return areas


# 안전영역의 최대 개수 리턴
def solution(N):
    # 답이 될 수 있는 값의 최소 = 1 (각 지점 높이 최소 = 1, 빗물 최소높이 = 0이므로)
    answer = 1
    for rain in range(1, 101):
        areas = calculate(N, rain)
        # 만약 특정 빗물 높이에 대해 안전영역이 0이면 break -> 빗물이 height의 최댓값과 같아진 거니까
        if areas == 0:
            break
        if answer < areas:
            answer = areas
    return answer

print(solution(N))
