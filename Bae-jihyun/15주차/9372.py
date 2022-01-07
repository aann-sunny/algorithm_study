'''
1. 비행기로 이동 가능한 나라를 양방향 그래프로 저장
2. bfs로 다음 나라로 이동할 때마다 cnt를 증가
3. 최종 결과 출력
'''
import sys


def bfs(x):
    q = [x]
    visited[x] = 1
    cnt = 0
    while q:
        now = q.pop(0)
        for i in air[now]:
            if visited[i] == 0:
                visited[i] = 1
                cnt += 1
                q.append(i)
    return cnt


input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    air = [[] for __ in range(N + 1)]
    visited = [0 for __ in range(N + 1)]
    result = 0

    # 양방향 그래프로 입력받기
    for i in range(M):
        a, b = map(int, input().split())
        air[a].append(b)
        air[b].append(a)

    # BFS 실행
    for i in range(1, N + 1):
        if visited[i] == 0:
            result += bfs(i)

    print(result)
