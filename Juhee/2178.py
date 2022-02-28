# https://www.acmicpc.net/problem/2178

from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = []

for _ in range(N):
    graph.append(list(input()))


# 동서남북
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):

    queue = deque()
    queue.append((x, y))

    while queue:  # 큐에 값이 없을 때까지 while문을 돌리기
        x, y = queue.popleft()  # 제일 앞에 저장된 좌표를 뽑기

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            # 반복이 진행되는 도중 continue문을 만나면 반복문의 끝으로 이동하여 다음 반복문으로 넘어간다.
            # 위치가 벗어나면
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            # 이동할 수 없는 칸
            if graph[nx][ny] == 0:
                continue
            # 이동 가능
            if graph[nx][ny] == 1:
                # 만약에 길이 있으면(1이면) 가 좌표의 체크 배열에 현재 값에 1을 더해 저장해준다.
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx, ny))

    return graph[N-1][M-1]


'''
[1, 0, 9, 10, 11, 12]
[2, 0, 8, 0, 12, 0]
[3, 0, 7, 0, 13, 14]
[4, 5, 6, 0, 14, 15]
'''
print(bfs(0, 0))
