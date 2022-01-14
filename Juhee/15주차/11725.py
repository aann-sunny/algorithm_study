"""
     1
    / \
   4   6
  / \   \
 2   7   3
          \
           5

--> 출력
2의 부모: 4
3의 부모: 6
4의 부모: 1
5의 부모: 3
6의 부모: 1
7의 부모: 4

1. Tree를 어떻게 담아야하는지. 입력 저장 방법
--> list를 이용해보자.
list[A]=B
list[B]=A
같은 배열의 원소들, list index 원소: 연결되어 있는 원소들.

2. 탐색을 어떻게 할건지.
--> DFS를 이용해서 위에서 밑으로 내려오고 parent를 채워줌.
같은 배열의 원소 중 어떻게 부모를 찾는지 의문이 있었는데 
위에서 부터 아래로 차례로 내려오기 때문에 재귀함수를 통해 찾을 수 있음.

"""
import sys

sys.setrecursionlimit(10 ** 9)  # 없으면 런타임 에러

N = int(sys.stdin.readline())
tree = [[] for _ in range(N + 1)]
parents = [0 for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)


def DFS(start, tree, parents):
    for i in tree[start]:
        if parents[i] == 0:
            parents[i] = start
            DFS(i, tree, parents)


DFS(1, tree, parents)

for i in range(2, N + 1):
    print(parents[i])
