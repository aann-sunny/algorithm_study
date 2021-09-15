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
        d[r][c] = 0
        new_r_c = [(r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)]    # 상 우 하 좌
        for nr, nc in new_r_c:
            if (1 <= nr <= M) and (1 <= nc <= N) and (MAP[r][c] < MAP[nr][nc]):
                d[r][c] += func(nr, nc)
        return d[r][c] 

print(func(M, N))


"""
태홍님 피드백을 보고 if문이 지저분하게 쓰인 걸 어떻게 고칠 수 있을지 생각하다
지현님 풀이를 보고 힌트를 얻음

2차원 배열 같은 걸 인풋으로 받고, 현재 위치에서 상/하/좌/우에 있는 값이 어떤지를 따질 때
평소에는 직접 상하좌우에 해당하는 인덱스를 하나하나 변수에 할당하고 이를 if문을 통해 확인하면서 
만약 그 인덱스들이 인덱스 범위를 넘어가는지 안 넘어가는지 확인했었지만,
현재 값의 인덱스로부터 상하좌우에 해당하는 인덱스 값들을 리스트같은 데에 두고
그 리스트를 돌면서 인덱스 범위를 넘는지 안 넘는지 살피면 코드를 좀 더 예쁘게 짤 수 있는 것 같다.

만약 상하좌우로 늘 정해진 칸만큼 움직이면서 살펴야 한다면
방향성분?에 대한 값들을 리스트로 만들어서 활용하면 깔끔하게 코드를 짤 수 있을 것 같다.
"""