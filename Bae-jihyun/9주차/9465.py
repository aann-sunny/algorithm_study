import sys

T = int(input())

for _ in range(T):
    n = int(input())
    lst = []
    result = [[0]*(n+1) for _ in range(2)]

    for _ in range(2):
        lst.append(list(map(int, sys.stdin.readline().split())))

    # 풀이 아래 참고
    for j in range(1, n+1):
        for i in range(2):
            result[i][j] = max(
                result[i][j-1], result[(i+1) % 2][j-1]+lst[i][j-1]
                )
    print(max(result[0][j], result[1][j]))


''' 풀이
1. 16번째 줄
    result[i][j-1] : 왼쪽에 있는 점수 = 현재까지 누적된 최대 점수
       vs
    result[(i+1) % 2][j-1]+lst[i][j-1] : 왼쪽 대각선에 있는 점수(덕분에 현재 스티커를 뗄 수 있음)와
                                        현재 뗄 스티커 점수를 합친 점수

2. 19번째 줄
    result[0][j]을 누적해 result[1][j]이 생긴 것이 아니므로 max를 취해줘야함.
'''

'''
풀이를 생각할때 맞는 풀이에 접근했음에도 자신감이 없어서 계속 다른 풀이를 고민했다..
풀고나니 제대로 result가 안들어가졌길래 print해봤다.
i->j이면 result[1][j]부분이 제대로 안 채워져 max값 계산을 제대로 할 수 없다.
for문의 위치가 j -> i여야한다는 것을 알았다.
'''
