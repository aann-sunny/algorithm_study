import sys
sys.setrecursionlimit(10**6) # RecursionError 방지

N = int(sys.stdin.readline())

tree = [[] for i in range(N + 1)]
A = [[1, 0] for i in range(N + 1)]                   # index를 루트노드로 갖는 새끼트리들의 얼리 수 [index가 얼리일 때, index가 얼리가 아닐 때]
calculated = [[False, False] for i in range(N + 1)]  # index를 루트노드로 갖는 새끼트리들의 얼리 수를 계산한 적 있는가(index가 얼리일 때, index가 얼리가 아닐 때)


for i in range(N - 1):
    u, v = map(int, sys.stdin.readline().split())
    tree[u].append(v)
    tree[v].append(u)

def getEarlyCount(tree, pnode, node, isEarly):    # node를 루트로 하는 트리에서 얼리인 애들의 개수 리턴. isEarly를 통해 그 노드가 얼리인지 아닌지
    if isEarly:                 # isEarly == True : node가 얼리라면
        if calculated[node][0]: # 그 노드가 얼리일 때의 얼리 개수를 구한 적 있다면
            return A[node][0]
        else:                   # 그 노드가 얼리일 때의 얼리 개수를 구한 적 없다면 -> 구하고 리턴해야 함
            calculated[node][0] = True   # 계산여부 처리 -> node가 얼리일 때의 얼리개수를 구한 적 있음을 기록
            for child_node in tree[node]:  # 자신과 인접한 노드들에 대해 계산해주는데
                if pnode != child_node:    # 인접한 노드가 내 부모 노드가 아닐때만 계산함
                    A[node][0] += min(getEarlyCount(tree, node, child_node, True), getEarlyCount(tree, node, child_node, False))
            return A[node][0]
    else:                       # isEarly == False : node가 얼리가 아니라면
        if calculated[node][1]: # 그 노드가 얼리가 아닐 때의 얼리 개수를 구한 적 있다면
            return A[node][1]
        else:                   # 그 노드가 얼리가 아닐 때의 얼리 개수를 구한 적 없다면 -> 구하고 리턴해야 함
            calculated[node][1] = True     # 계산여부 처리 -> node가 얼리가 아닐 때의 얼리개수를 구한 적 있음을 기록
            for child_node in tree[node]:  # 자신과 인접한 노드들에 대해 계산해주는데
                if pnode != child_node:    # 인접한 노드가 내 부모 노드가 아닐때만 계산함
                    A[node][1] += getEarlyCount(tree, node, child_node, True)
            return A[node][1]

print(min(getEarlyCount(tree, 0, 1, True), getEarlyCount(tree, 0, 1, False)))