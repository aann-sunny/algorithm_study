# 백준 1260 - DFS와 BFS(https://www.acmicpc.net/problem/1260)

"""
참고한 링크
https://itholic.github.io/python-bfs-dfs/
https://cyc1am3n.github.io/2019/04/26/bfs_dfs_with_python.html
"""
"""
BFS, DFS 및 그래프?를 처음 배우게 되면서
BFS, DFS를 어떤 식으로 구현하는게 효율적인지 고민해본 문제
사실 풀었다기보다는 BFS, DFS가 이런 거구나 같은 걸 알게 된 것 같다
"""

from collections import deque
import sys

def BFS(graph, start_node):
    visited = {}
    queue = deque([start_node])

    while queue:
        node = queue.popleft()         # 현재 큐에서 가장 처음에 들어간 애 빼오기
        if node not in visited:        
            visited[node] = True
            print(node, end=' ')        # 개행 없이 출력되도록
            not_visited_nodes = list((set(graph[node]) - set(visited)))  # not_visited_node : 방금 큐에서 빼온 애랑 연결된 애들 중에 방문한 적 없는 애들
            queue += sorted(not_visited_nodes)

def DFS(graph, start_node):
    visited = {}
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited[node] = True
            print(node, end=' ')         # 개행 없이 출력되도록
            not_visited_nodes = list(set(graph[node]) - set(visited))    # not_visited_node : 방금 스택에서 빼온 애랑 연결된 애들 중에 방문한 적 없는 애들
            stack += sorted(not_visited_nodes, reverse=True)    # 거꾸로 정렬해서 스택에 넣지 않으면 출력값이 달라져서 이렇게 함


graph = {}
N, M, V = map(int, sys.stdin.readline().split())

"""
찾아보니까 그래프를 딕셔너리를 통해서 어떤 원소?가 있으면 걔를 key로 하고 
그 원소에 연결된 원소들을 리스트로 묶어서 value로 하는 것 같아서 이렇게 해봤다 ↓
"""
for i in range(M):
    inputs = list(map(int, sys.stdin.readline().split()))
    if inputs[0] in graph:
        graph[inputs[0]].append(inputs[1])
    else:
        graph[inputs[0]] = [inputs[1]]
    if inputs[1] in graph:
        graph[inputs[1]].append(inputs[0])
    else:
        graph[inputs[1]] = [inputs[0]]

if V not in graph:             # 연결된 원소들이 있어야 graph에 key로 존재하는데, 만약 시작점과 연결된 원소들이 하나도 없다면 시작점이 graph에 key로 없어서 keyError가 생기는 걸 방지
    graph[V] = []              # 아니면 DFS, BFS를 정의한 함수에서 내가 방금 스택(or 큐)에서 빼온 원소가 graph에 있어야지 연결된 원소들을 스택(or 큐)에 추가하게끔 동작하게 만들 수도 있을 것 같다

for node in graph:
    graph[node].sort()

DFS(graph, V)
print()
BFS(graph, V)