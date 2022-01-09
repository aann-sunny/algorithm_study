"""
11752와 유사한 문제

주어지는 비행 스케줄은 항상 연결 그래프를 이룬다. -->
여행지가 다 연결되어 있으면 연결된 선 개수만 세면 되는거 아닌가??
"""
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    tree = [[] for _ in range(M + 1)]
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        # tree[a].append(b)
        # tree[b].append(a)

    print(N - 1)
