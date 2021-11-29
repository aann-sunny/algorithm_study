N, result = int(input()), 0
a, b, c = [False]*N, [False]*(2*N-1), [False]*(2*N-1)
# a : 세로 줄
# b : 오른쪽 상단 왼쪽 하단 대각선
# c : 왼쪽 상단 오른쪽 하단 대각선


def solve(i):
    global result
    if i == N:  # 재귀가 n번 반복됐다는 것은 퀸 n개를 놓는데 성공했다는 뜻
        result += 1
        return
    for j in range(N):
        if not (a[j] or b[i+j] or c[i-j+N-1]):  # 세로줄과 대각선들에 퀸이 없다면
            a[j] = b[i+j] = c[i-j+N-1] = True   # 퀸을 둔다.
            solve(i+1)
            a[j] = b[i+j] = c[i-j+N-1] = False  # 들어갔다가 나올때 false로 해줘야 다음에도 사용


solve(0)
print(result)


'''
※ c[i-j+N-1] : i-j로 왼쪽상단 오른쪽 하단인 대각선을 만들 수 있는데 +N-1을 해줘야 음수가 되지 않는다.

출처: https://rebas.kr/761 [PROJECT REBAS]
    https://blog.encrypted.gg/945
'''
