import sys

read = sys.stdin.readline
sys.setrecursionlimit(10000)

visited = []
anw = []

# 동서남북대각선 모든 방향
dx = [1, 1, -1, -1, 1, -1, 0, 0]
dy = [0, 1, 0, 1, -1, -1, 1, -1]


def dfs(x, y):
    graph[x][y] = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < b and 0 <= ny < a and graph[nx][ny] == 1:
            dfs(nx, ny)


while True:
    a, b = map(int, read().split())
    if a == 0 and b == 0:
        break
    graph = []
    anw = 0
    for _ in range(b):
        graph.append(list(map(int, read().split())))
    for i in range(b):
        for j in range(a):
            if graph[i][j] == 1:
                dfs(i, j)  # 끝까지 내려갔다가 옆으로 갈때 anw+1
                anw += 1
    print(anw)
