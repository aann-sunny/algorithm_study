'''
1. 비행기로 이동 가능한 나라를 양방향 그래프로 저장
2. bfs로 다음 나라로 이동할 때마다 cnt를 증가
3. 최종 결과 출력
'''
import sys
from collections import deque


def bfs(x):
    q = deque([x])
    visited[x] = 1
    cnt = 0
    while q:
        now = q.popleft()
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

    # 양방향 그래프로 입력받기 (인접리스트)
    for i in range(M):
        a, b = map(int, input().split())
        air[a].append(b)
        air[b].append(a)

    # BFS 실행
    for i in range(1, N + 1):
        if visited[i] == 0:
            result += bfs(i)

    print(result)

'''
deque와 queue의 차이
deque : double-ended queue의 약자로 양방향에서 데이터 추가/제거 할 수 있는 자료구조
        list와 비슷하게 동작하지만, list보다 deque가 더 빠르게 동작하도록 설계
Queue : 주로 멀티 쓰레딩 환경에서 사용, 내부적으로 락킹(locking)을 지원하여
        여러 개의 쓰레드가 동시에 데이터를 추가하거나 삭제가능 ( 방향성 없음 )
'''
