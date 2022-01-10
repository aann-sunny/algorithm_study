import sys
from collections import deque


def dfs(start, visited=[]):       # 반복되는 일 : dict의 values([정점, 정점,])를 순회하기
    visited.append(start)           # 정점을 visited에 추가

    for node in graph[start]:       # 정점과 이어진 node들이
        if node not in visited:     # 만약 visited에 없다면
            dfs(node, visited)      # dfs 다시 실행(visited에 추가하고 정점과 이어진 노드로 이동)
    return visited


def bfs(start):                             # queue 맨 뒤에 순서대로 넣고 앞쪽부터 빼기
    visited, queue = set(), deque([start])  # visited : 출력된 정점, queue : 출력 될 정점
    visited.add(start)

    while queue:
        vertex = queue.popleft()          # 제일 왼쪽 정점 빼기
        print(str(vertex) + " ", end="")  # 정점 출력

        for node in graph[vertex]:        # node : 출력될 정점들
            if node not in visited:       # 출력될 정점이 이미 출력된 정점이 아니라면
                visited.add(node)         # 출력된 정점에 넣고
                queue.append(node)        # 출력될 정점에도 넣는다.


n, m, v = map(int, sys.stdin.readline().strip().split())  # 입력 받기
graph = dict()

for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    if a in graph:                      # graph안에 a가 있다면
        graph[a].append(b)              # a의 value인 배열에 b를 추가
    else:                               # graph안에 a가 없다면
        graph[a] = [b]                  # a의 value인 배열을 만들고 b를 추가
    if b in graph:
        graph[b].append(a)
    else:
        graph[b] = [a]

for value in graph.values():            # 각 정점과 연결된 정점들 sort
    value.sort()
print(graph)

result = dfs(v)
for i in result:
    print(str(i) + " ", end="")
print()
bfs(v)


'''
def dfs2(graph, start_node):
    ## deque 패키지 불러오기
    from collections import deque
    visited = []
    need_visited = deque()

    ##시작 노드 설정해주기
    need_visited.append(start_node)

    ## 방문이 필요한 리스트가 아직 존재한다면
    while need_visited:
        ## 시작 노드를 지정하고
        node = need_visited.popleft()

        ##만약 방문한 리스트에 없다면
        if node not in visited:

            ## 방문 리스트에 노드를 추가
            visited.append(node)
            ## 인접 노드들을 방문 예정 리스트에 추가
            need_visited.extend(graph[node])

    return visited
'''
