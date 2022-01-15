'''
1. 인접행렬로 트리를 입력받고 루트를 찾아준다.
2. 열의 위치를 1씩 늘려가며 서브트리를 찾고 res에 최소, 최대 너비를 갱신해간다.
3. ans에 각 레벨별 너비를 계산해 [너비, 레벨]을 넣는다.
4. 조건에 맞게 정렬해 결과를 출력해준다.
조건 : 너비가 가장 넓은 레벨과 그 레벨의 너비를 출력. 너비가 가장 넓은 레벨이 두 개 이상 있을 때엔 번호가 작은 레벨을 출력.
'''

import sys


# dfs : 현재 노드 번호가 num이고 깊이가 depth일 때 노드 위치를 구하는 함수
def dfs(num, depth):
    global cnt  # 열의 위치
    # Base Case : 노드 번호가 유효하지 않은 경우
    if num == -1:
        return
    # 현재 depth가 dictionary에 없다면 해당 깊이에서의 [최소 위치, 최대 위치]로 초기화
    if depth not in res:
        res[depth] = [9876543210, -9876543210]
    # 왼쪽 서브트리
    dfs(tree[num][0], depth + 1)
    # 최소, 최대 너비 갱신
    res[depth][0] = min(res[depth][0], cnt)  # 현재까지 최소 열과 현재 열 중 누가 더 작은 수인지 비교
    res[depth][1] = max(res[depth][1], cnt)
    # 열의 위치 증가
    cnt += 1
    # 오른쪽 서브트리
    dfs(tree[num][1], depth + 1)


N = int(sys.stdin.readline())

# tree : N X 2 행렬로, i번째 행 0번째 열은 왼쪽 자식, i번째 행 1번째 열은 오른쪽 자식을 저장
tree = [[-1] * 2 for _ in range(N + 1)]

# res : depth를 key, [최소 위치, 최대 위치]를 value로 하는 dictionary
res = dict()
cnt = 1

# isRoot : 전입 차수, 루트 판별용도
isRoot = [0] * (N + 1)

# 입력받기
for _ in range(N):
    value, left, right = map(int, sys.stdin.readline().split())
    if left != -1:
        tree[value][0] = left
        isRoot[left] += 1  # 자식노드(left)에개 부모가 있다는 표시
    if right != -1:
        tree[value][1] = right
        isRoot[right] += 1

root = -1
for i in range(1, N + 1):
    # 루트이기에 전입 차수는 0 (루트노드는 부모가 없다.)
    if not isRoot[i]:
        root = i

# 중위 순회
dfs(root, 1)

# 각 레벨별 너비 계산 [너비, 레벨]
ans = []
for i in res:
    ans.append((res[i][1] - res[i][0] + 1, i))

# 문제 조건에 따라 정렬 후 정답 출력
ans.sort(key=lambda x: (-x[0], x[1]))
print(ans[0][1], ans[0][0])


'''
전입 차수 : 정점으로 들어오는 간선의 수
'''

'''
인접행렬
- adj[i][j] : 노드 i에서 j로 가는 간선이 존재할 경우 1, 아니면 0
장점 : 구현이 간단
단점 : 노드의 개수 대비 간선의 개수가 적으면 효율이 떨어진다.

인접리스트
- adj[i] : i번쨰 노드에 연결된 노드들을 원소로 갖는 리스트
장점 : 간선의 개수에 비례하는 메모리만 차지
단점 : 노드 i와 노드 j의 연결 여부를 알고싶을땐 리스트를 순회하여 i원소가 존재하는지 확인해야함.
O(V)의 시간복잡도를 갖게 된다.

참고자료
https://duwjdtn11.tistory.com/515
'''
