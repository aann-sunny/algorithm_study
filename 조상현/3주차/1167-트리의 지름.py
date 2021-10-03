# 백준 1167 - 트리의 지름(https://www.acmicpc.net/problem/1260)

"""
 처음에는 단순히 DFS를 통해 루트노드에서 끝노드까지 측정되는 거리 중에 최대값을 출력하면 될 거라 생각했지만,
 풀다보니 루트노드를 도대체 무슨 노드로 설정해줄 건지에 대한 문제?가 생겼다
 x라는 임의의 노드에서 측정했을 때 y가 가장 먼 거리의 노드라고 할 때
 y에서 측정한 최장거리 노드도 x라면 이 거리가 최대거리라고 생각했다(결국 최장거리는 끝점과 끝점 사이의 거리 중 하나이므로)
 그러나 두 번의 최대거리 측정 결과가 같아질때까지 DFS를 돌리는 건 좀 아닌 것 같아서
 관련된 걸 찾아보다가 다음 링크를 참고하ㅐㅆ다

 https://blog.myungwoo.kr/112
 임의의 노드에서 가장 멀리 있는 노드를 찾은 다음, 그 노드를 루트 노드로 거리를 측정하면
 측정된 거리중 가장 긴 거리가 최대거리

 DFS를 돌려서 가장 먼 노드를 찾고,
 그 노트를 루트노드로 한 번 더 DFS를 돌려서 가장 먼 거리를 찾는다

"""
import sys
sys.setrecursionlimit(10**6) # RecursionError 방지

V = int(sys.stdin.readline())
Tree = [[] for i in range(V + 1)]

for i in range(V):
    c = list(map(int, sys.stdin.readline().split()))
    for j in range(1, len(c) - 1, 2):
        Tree[c[0]].append([c[j], c[j + 1]])  # 각 노드에 연결된 노드와 간선의 길이 표현


def DFS(Tree, start_node, distance):
    for node, dis in Tree[start_node]:
        if not distance[node]:               # node까지 가는 거리가 0이라면 (기록되지 않았다면)
            distance[node] = distance[start_node] + dis  # node까지 가는 거리 기록
            DFS(Tree, node, distance)

distance = [0 for i in range(V + 1)]
start_node = DFS(Tree, 1, distance)
distance[1] = 0                           # distance는 start_node에서 각 노드까지의 거리를 저장하는 리스트이므로, 자기 자신에서 출발해 자기 자신까지의 거리는 0으로 해야 함.

start_node, max_distance = -1, -1

for i in range(1, V + 1):
    if distance[i] > max_distance:
        max_distance = distance[i]
        start_node = i

distance = [0 for i in range(V + 1)]
DFS(Tree, start_node, distance)
distance[start_node] = 0                  # distance는 start_node에서 각 노드까지의 거리를 저장하는 리스트이므로, 자기 자신에서 출발해 자기 자신까지의 거리는 0으로 해야 함.
print(max(distance))