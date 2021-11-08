# 완료
from collections import deque
import sys


# O(N^2) --> O(dfs번*N) dfs번: 이진 트리에서의 높이


def dfs(V):
    print(V, end=" ")
    visited[V] = True  # 첫 노드 방문
    for i in range(1, N + 1):
        if visited[i] is False and graph[V][i] == 1:  # 방문X, 노드 연결되어있다면
            dfs(i)


# 큐 이용  O(N^2) --> O(dfs번*N)
def bfs(V):
    queue = deque([V])
    visited[V] = True
    while queue:
        V = queue.popleft()  # 가장 밑에 있는걸(가장 먼저 들어온 것) 빼고 V에 저장
        print(V, end=" ")
        for i in range(1, N + 1):
            if visited[i] is False and graph[V][i] == 1:  # 방문X, 노드 연결되어있다면
                queue.append(i)
                visited[i] = True


N, M, V = map(int, sys.stdin.readline().split())
graph = [[0] * (N + 1) for i in range(N + 1)]
visited = [False for i in range(N + 1)]  # 방문 여부

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1  # 양뱡향이므로

dfs(V)
print()
visited = [False for i in range(N + 1)]
bfs(V)

"""
import collections
import sys

#재귀를 이용하여 가장 깊이 이동
def dfs(V):
    print(V,end=' ')
    visited[V]=True  #첫 노드 방문
    for i in range(1,N+1):
        if visited[i]==False and graph[V][i]==1:  #방문X, 노드 연결되어있다면
            dfs(i)  

#큐 이용          
def bfs(V):
    queue=[V]
    visited[V]=True
    while(queue):
        V=queue.pop(0) #가장 밑에 있는걸(가장 먼저 들어온 것) 빼고 V에 저장
        print(V,end=' ')
        for i in range(1,N+1):
            if visited[i]==False and graph[V][i]==1: #방문X, 노드 연결되어있다면
                queue.append(i)
                visited[i]=True

N,M,V = map(int,sys.stdin.readline().split())
graph=[[0]*(N+1) for i in range(N+1)]
visited=[False for i in range(N+1)]  #방문 여부

for i in range(M):
    a,b = map(int,sys.stdin.readline().split())
    graph[a][b]=1
    graph[b][a]=1  #양뱡향이므로

dfs(V)
print()
visited=[False for i in range(N+1)]
bfs(V)

피드백 코멘트 :
파이썬에서 큐의 pop 연산을 list.pop(0)로 구현하면 성능이 좋지 않습니다.
deque에 대해 알아보시면 좋을 듯 합니다!
"""
