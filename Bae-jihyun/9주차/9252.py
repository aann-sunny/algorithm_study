first = input()
second = input()
dp = [[0]*(len(first)+1) for _ in range(len(second)+1)]

r = 1
c = 1

# dp 만들기
for j in first:          # c가 늘어나야함.
    for i in second:     # r이 늘어나야함.
        if i == j:
            dp[r][c] = dp[r-1][c-1]+1  # LCS에 i와 j를 추가하기 전보다 1개 늘어남.
        else:
            dp[r][c] = max(dp[r][c-1], dp[r-1][c])
        r += 1
    c += 1
    r = 1


# LCS 찾기
result = ""

target = dp[-1][-1]  # 맨 끝 점
y = len(dp) - 1
x = len(dp[0]) - 1

while target != 0:
    # 아래 풀이 참고
    if dp[y][x - 1] == target - 1 and dp[y - 1][x] == target-1:
        result = first[x - 1] + result
        target -= 1
        y -= 1    # 대각선으로 이동
        x -= 1
    else:  # LCS아님.
        if dp[y - 1][x] > dp[y][x - 1]:
            y -= 1
        else:
            x -= 1

# 결과 출력
print(dp[-1][-1])
if len(result) != 0:
    print(result)


''' 풀이
1. 29번째 줄
    현재 값보다 왼쪽칸, 윗칸의 값들이 모두 1씩 작다면 LCS 문자이므로
    result에 넣고 대각선으로 이동.
2. 34번째 줄
    그렇지 않다면, 윗칸이나 왼쪽 칸중 더 큰 값이 있는 곳으로 이동.
'''
