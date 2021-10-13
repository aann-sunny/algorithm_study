# 최장 거리 계산 문제는 DFS가 좋을 것 같다고 생각
import sys

V = int(sys.stdin.readline())
graph = [[0] * (V + 1) for i in range(V + 1)]
visited = [False for i in range(V + 1)]  # 방문 여부


def dfs(V):
    print(V, end=" ")
    visited[V] = True  # 첫 노드 방문
    for i in range(1, V + 1):
        if visited[i] is False and graph[V][i] == 1:  # 방문X, 노드 연결되어있다면
            dfs(i)


# 입력 받기
for i in range(V):
    num_list = list(map(int, sys.stdin.readline().split()))
    for j in range(1, len(num_list) - 1, 2):
        graph[num_list[0]][num_list[j]] = num_list[j + 1]


# 아직 진행 중
