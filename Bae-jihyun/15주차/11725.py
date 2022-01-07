'''
처음 방문하는 노드마다 그 노드를 탐색한 직전의 노드 번호를 기록해준 뒤 출력.
dfs 로 들어가면서 방문하지 않았다면, dfs 들어가는 노드가 자식, 현재 확인하고 있는 노드가 부모 노드이다.
'''

import sys
sys.setrecursionlimit(10**6)


def dfs(n):
    for i in tree[n]:   # tree[n] : 부모나 자식노드
        if result[i] == -1:
            result[i] = n
            # 이제 result[i] : 부모노드
            dfs(i)


input = sys.stdin.readline
N = int(input())
tree = [[] for _ in range(N+1)]
result = [-1]*(N+1)

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)


dfs(1)    # 트리의 루트를 1이라고 임의로 가정
for i in range(2, N+1):  # 부모 노드 번호를 2번 노드부터 순서대로 출력
    print(result[i])
