# 백준 2533 - SNS (https://www.acmicpc.net/problem/2533)
"""
문제의 조건 상자신의 모든 친구가 얼리여야만 함 따라서 1 - 2 - 3 - 4로 연결됐을 때 1, 4가 얼리인 것은 소용 X

감이 안 잡혀서 이 문제를 풀 수 있는 힌트를 찾았음
-> 자식이 있는 노드는 본인이 얼리가 아니면 자식이 얼리여야 함
-> 본인이 얼리 -> 자식은 아닐수도?
이걸 활용해서 풀어보기로 했다

1을 루트노드로 하는 트리의 얼리 수
1) 1이 얼리일 때, 1의 자식들을 루트노드로 갖는 새끼트리들의 얼리수들의 합
2) 1이 얼리가 아닐 때, 1의 자식들을 루트노드로 갖는 새끼트리들의 얼리수들의 합
중 작은 값

본인의 자식들이 루트노드인 새끼트리들의 얼리수들이 합이 되는 이유?
-> 각 새끼트리들이 독립적이라 서로에게 영향을 안 주니까.
"""

# import sys
# sys.setrecursionlimit(10**6) # RecursionError 방지

# N = int(sys.stdin.readline())

# tree = [[] for i in range(N + 1)]
# A = [[1, 0] for i in range(N + 1)]                   # index를 루트노드로 갖는 새끼트리들의 얼리 수 [index가 얼리일 때, index가 얼리가 아닐 때]
# calculated = [[False, False] for i in range(N + 1)]  # index를 루트노드로 갖는 새끼트리들의 얼리 수를 계산한 적 있는가(index가 얼리일 때, index가 얼리가 아닐 때)


# for i in range(N - 1):
#     u, v = map(int, sys.stdin.readline().split())
#     tree[u].append(v)

# def getEarlyCount(tree, node, isEarly):    # node를 루트로 하는 트리에서 얼리인 애들의 개수 리턴. isEarly를 통해 그 노드가 얼리인지 아닌지
#     if isEarly:                 # isEarly == True : node가 얼리라면
#         if calculated[node][0]: # 그 노드가 얼리일 때의 얼리 개수를 구한 적 있다면
#             return A[node][0]
#         else:                   # 그 노드가 얼리일 때의 얼리 개수를 구한 적 없다면 -> 구하고 리턴
#             calculated[node][0] = True   # 계산여부 처리 -> node가 얼리일 때의 얼리개수를 구한 적 있음을 기록
#             for child_node in tree[node]:
#                 A[node][0] += min(getEarlyCount(tree, child_node, True), getEarlyCount(tree, child_node, False))
#             return A[node][0]
#     else:                       # isEarly == False : node가 얼리가 아니라면
#         if calculated[node][1]: # 그 노드가 얼리가 아닐 때의 얼리 개수를 구한 적 있다면
#             return A[node][1]
#         else:                   # 그 노드가 얼리가 아닐 때의 얼리 개수를 구한 적 없다면 -> 구하고 리턴
#             calculated[node][1] = True     # 계산여부 처리 -> node가 얼리가 아닐 때의 얼리개수를 구한 적 있음을 기록
#             for child_node in tree[node]:
#                 A[node][1] += getEarlyCount(tree, child_node, True)
#             return A[node][1]

# print(min(getEarlyCount(tree, 1, True), getEarlyCount(tree, 1, False)))
    
"""
틀렸습니다가 나옴. 생각해보니까 항상 1이 루트노드로 주어지는 게 아니여서 그런 것 같다

좀 더 생각해보니까 1을 루트노드로 가정하고 한 건 상관이 없는데, 
트리를 표현해줄 때 자신과 인접한 노드 중 자식노드?만 표현해준 것이 원인같다. ex) 1 4로 입력이 들어오면 tree[1]에만 4를 추가하고 tree[4]엔 1을 추가 안 함
부모노드까지 표현해주되 따로 부모에 대한? 방문처리를 해주기로 함

-> getEarlyCount를 호출할 때, 자기자신도 파라미터로 넣어주어
자신을 호출한 부모가 누군지 알게 함
"""
# ---------------------------------------------------------------------------------------------------------------------------------------------------------#

# import sys
# sys.setrecursionlimit(10**6) # RecursionError 방지

# N = int(sys.stdin.readline())

# tree = [[] for i in range(N + 1)]
# A = [[1, 0] for i in range(N + 1)]                   # index를 루트노드로 갖는 새끼트리들의 얼리 수 [index가 얼리일 때, index가 얼리가 아닐 때]
# calculated = [[False, False] for i in range(N + 1)]  # index를 루트노드로 갖는 새끼트리들의 얼리 수를 계산한 적 있는가(index가 얼리일 때, index가 얼리가 아닐 때)


# for i in range(N - 1):
#     u, v = map(int, sys.stdin.readline().split())
#     tree[u].append(v)
#     tree[v].append(u)

# def getEarlyCount(tree, pnode, node, isEarly):    # node를 루트로 하는 트리에서 얼리인 애들의 개수 리턴. isEarly를 통해 그 노드가 얼리인지 아닌지
#     if isEarly:                 # isEarly == True : node가 얼리라면
#         if calculated[node][0]: # 그 노드가 얼리일 때의 얼리 개수를 구한 적 있다면
#             return A[node][0]
#         else:                   # 그 노드가 얼리일 때의 얼리 개수를 구한 적 없다면 -> 구하고 리턴해야 함
#             calculated[node][0] = True   # 계산여부 처리 -> node가 얼리일 때의 얼리개수를 구한 적 있음을 기록
#             for child_node in tree[node]:  # 자신과 인접한 노드들에 대해 계산해주는데
#                 if pnode != child_node:    # 인접한 노드가 내 부모 노드가 아닐때만 계산함
#                     A[node][0] += min(getEarlyCount(tree, node, child_node, True), getEarlyCount(tree, node, child_node, False))
#             return A[node][0]
#     else:                       # isEarly == False : node가 얼리가 아니라면
#         if calculated[node][1]: # 그 노드가 얼리가 아닐 때의 얼리 개수를 구한 적 있다면
#             return A[node][1]
#         else:                   # 그 노드가 얼리가 아닐 때의 얼리 개수를 구한 적 없다면 -> 구하고 리턴해야 함
#             calculated[node][1] = True     # 계산여부 처리 -> node가 얼리가 아닐 때의 얼리개수를 구한 적 있음을 기록
#             for child_node in tree[node]:  # 자신과 인접한 노드들에 대해 계산해주는데
#                 if pnode != child_node:    # 인접한 노드가 내 부모 노드가 아닐때만 계산함
#                     A[node][1] += getEarlyCount(tree, node, child_node, True)
#             return A[node][1]

# print(min(getEarlyCount(tree, 0, 1, True), getEarlyCount(tree, 0, 1, False)))

"""
맞긴 한데 넘 복잡한 것 같아서 
다른 사람들 풀이를 보다가 새끼트리를 구할 때 루트가 얼리인 애를 구했는지, 얼리가 아닌 애를 구했는지를
따로 계산여부를 기록하지 않고 그냥 방문처리만 해줄 수 있음을 알게 됐다."""

# ---------------------------------------------------------------------------------------------------------------------------------------------------------#

import sys
sys.setrecursionlimit(10**6) # RecursionError 방지

N = int(sys.stdin.readline())

tree = [[] for i in range(N + 1)]
A = [[1, 0] for i in range(N + 1)]                # index를 루트노드로 갖는 새끼트리들의 얼리 수 [index가 얼리일 때, index가 얼리가 아닐 때]
visited = [False for i in range(N + 1)]           # index를 방문한 적 있는가


for i in range(N - 1):
    u, v = map(int, sys.stdin.readline().split())
    tree[u].append(v)
    tree[v].append(u)                             # 양방향 처리

def getEarlyCount(tree, node, isEarly):    # node를 루트로 하는 트리에서 얼리인 애들의 개수 리턴. isEarly를 통해 그 노드가 얼리인지 아닌지
    visited[node] = True
    for child_node in tree[node]:
        if not visited[child_node]:        # 아예 그냥 node가 얼리일 때와 아닐 때를 한 함수 실행 내에서 구함
            A[node][0] += min(getEarlyCount(tree, child_node, True), getEarlyCount(tree, child_node, False))
            A[node][1] += getEarlyCount(tree, child_node, True)
    if isEarly == True:
        return A[node][0]
    else:
        return A[node][1]

print(min(getEarlyCount(tree, 1, True), getEarlyCount(tree, 1, False)))