# 백준 2533 - SNS (https://www.acmicpc.net/problem/2533)
"""
문제의 조건 상자신의 모든 친구가 얼리여야만 함 따라서 1 - 2 - 3 - 4로 연결됐을 때 1, 4가 얼리인 것은 소용 X
-> 자식이 있는 노드는 본인이 얼리가 아니면 자식이 얼리여야 함
-> 본인이 얼리 -> 자식은 아닐수도?

1을 루트노드로 하는 트리의 얼리 수
1) 1이 얼리일 때, 1의 자식들을 루트노드로 갖는 새끼트리들의 얼리수들의 합
2) 1이 얼리가 아닐 때, 1의 자식들을 루트노드로 갖는 새끼트리들의 얼리수들의 합
중 작은 값
"""

import sys
sys.setrecursionlimit(10**6) # RecursionError 방지

N = int(sys.stdin.readline())

tree = [[] for i in range(N + 1)]
A = [-1 for i in range(N + 1)]              # index를 루트노드로 갖는 새끼트리들의 얼리 수 저장

for i in range(N - 1):
    u, v = map(int, sys.stdin.readline().split())
    tree[u].append(v)

