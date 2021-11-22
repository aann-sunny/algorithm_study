# 오류
import sys

N = int(sys.stdin.readline())
num_list = []
visited = []
maxnum = 0
ans = 0

# 동서남북
dx = [1, -1, 0, 0]
dy = [1, -1, 0, 0]


def dfs(x, y, h):
    for m in range(4):
        nx = x + dx[m]
        ny = y + dy[m]
        if (0 <= nx < N) and (0 <= ny < N) and num_list[nx][ny] > h:
            dfs(nx, ny, h)


for _ in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    if max(a) > maxnum:
        maxnum = max(a)
    num_list.append(a)

ans_list = []
for i in range(1, maxnum + 1):
    ans = 0
    for a in range(N):
        for b in range(N):
            if num_list[a][b] > i:
                ans += 1
                dfs(a, b, i)
    ans_list.append(ans)

print(max(ans_list))
