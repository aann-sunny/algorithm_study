first = input()
second = input()
board = [[0]*(len(first)+1) for _ in range(len(second)+1)]

r = 1
c = 1

for j in first:          # c가 늘어나야함.
    for i in second:     # r이 늘어나야함.
        if i == j:
            board[r][c] = board[r-1][c-1]+1  # LCS에 i와 j를 추가하기 전보다 1개 늘어남.
        else:
            board[r][c] = max(board[r][c-1], board[r-1][c])
        r += 1
    c += 1
    r = 1

print(board[-1][-1])


''' 풀이
1. 11번째 줄
    board[r][c] = board[r][c-1]+1 인줄알았는데
    ACAYAP, CAP로 반례를 찾았다.
    그래서 i와 j가 추가되기 전인 board[r-1][c-1](대각선 왼쪽위)에 1을 추가해주어야 한다.

2. 13번째 줄
    LCS 값이 누적되므로 윗칸과 왼쪽칸을 비교해 max를 취해준다.
'''
