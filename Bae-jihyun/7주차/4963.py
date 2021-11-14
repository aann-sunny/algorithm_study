import sys
sys.setrecursionlimit(10 ** 9)

direction = [
    (0, -1), (0, 1), (-1, 0), (1, 0),
    (1, -1), (-1, 1), (1, 1), (-1, -1)
]
ground = []   # lands
count = 0


def cal(c, r):
    # 방문 여부 체크
    if board[c][r] != -1:
        return
    board[c][r] = 0                            # 방문했다 표시.

    # 갈 수 있는 길 끝까지 방문해 전부 방문표시를 한다. (다시 방문하지 않게)
    for dc, dr in direction:
        nc = c + dc                               # 다음 c좌표구하기
        nr = r + dr                               # 다음 r좌표구하기

        if 0 <= nc < h and 0 <= nr < w:         # 다음 c, r좌표가 유효한지
            if ground[nc][nr] == 1 and board[nc][nr] == -1:
                cal(nc, nr)


while 1:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    board = [[-1] * w for _ in range(h)]     # 각 land가 계산되었는지 알아보는 board

    for _ in range(h):
        ground.append(list(map(int, sys.stdin.readline().split())))

    for c in range(h):
        for r in range(w):

            # 0인 곳은 갈 필요가 없고 방문한 1들은 걸러주면서 시간줄이기
            if ground[c][r] == 1 and board[c][r] == -1:
                count = count+1
                cal(c, r)

    print(count)

    # 초기화
    ground = []
    board = []
    count = 0


'''
풀이 생각과정
0, 0부터 더 이상 갈 길이 없을때까지 재귀를 돌린다. 섬 1개까지만 찾을 수 있음
=> 그렇다고 전부 for문을 돌리면 시간낭비
=> 방문한 이력 저장시키고, 방문 안했는데 갈 수 있는 길(1인 땅)만 계산돌리기

x, y 로 두고 풀었더니 너무 혼란이 와서 앞으로 이런 문제는 r, c로 풀고 그림보다 배열(ground)을 보고 풀자.
ground[y][x]
원래 for y 아래 for x 순서고 for r 아래 for c순서.
'''
