# 백준 1520 - 내리막길(https://www.acmicpc.net/problem/1520)
import sys
sys.setrecursionlimit(10000) # RecursionError 방지
MAP = []

M, N = map(int, sys.stdin.readline().split())
MAP.append([0 for i in range(N + 2)])

for i in range(M):
    heights = [0] + list(map(int, sys.stdin.readline().split())) + [0]
    MAP.append(heights)                     # M, N, 각 지점의 높이 입력받기 
MAP.append([0 for i in range(N + 2)])       # MAP은 사용자로부터 입력받은 각 지점의 높이들을 0들이 둘러싼 형태가 됨

d = [[-1]*(N + 2) for i in range(M + 2)]    # 시작점으로부터 각 지점까지 갈 수 있는 경로개수 저장하는 리스트, 전부다 -1로 초기화
d[1][1] = 1                                 # 시작점

def func(r, c):           # MAP[r][c] 까지 오는 경로의 개수를 리턴하는 함수
    if d[r][c] != -1:     # d[r][c] != 1 -> 이미 그 경로까지 가는 개수를 구한 것이므로 다시 구할 필요 X
        return d[r][c]
    else:
        if r == 0 or c == 0 or r > M or c > N:
            return 0
        else:
            top, left, right, bottom = 0, 0, 0, 0     # 각 방향으로부터의 경로 수
            
            if MAP[r - 1][c] > MAP[r][c]:
                top = func(r - 1, c)
        
            if MAP[r][c - 1] > MAP[r][c]:
                left = func(r, c - 1)
        
            if MAP[r + 1][c] > MAP[r][c]:
                bottom = func(r + 1, c)
        
            if MAP[r][c + 1] > MAP[r][c]:
                right = func(r, c + 1)

            d[r][c] = top + left + right + bottom
            return d[r][c]

print(func(M, N))


"""
피드백 코멘트 :
중간 부분에 4중 if문이 있는데요, 하나로 합칠 방법이 있지 않을까요?
일반화해서 표현하는 연습을 해보셔도 좋을 것 같습니다. 
"""
