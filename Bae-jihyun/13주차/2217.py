'''
W = 각 중량 * 각 들 수 있는 중량보다 큰 로프의 수

예를 들어
N = 5, 각 들 수 있는 중량이 5 10 20 30 40 일 때
최대 중량은
5*5 = 25
10*4 = 40
20*3 = 60
30*2 = 60
40*1 = 40 으로 60이다.

요점!
sort된 데이터의 각 중량마다, 들 수 있는 최대중량을 구하고 max값과 비교한다.
max값보다 크면 max을 갱신시킨다.
N의 범위가 100,000이므로 max 값을 구하고 비교해주면 O(n)으로 시간초과는 나지 않는다.
'''

N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))

lst.sort()

max = lst[0] * N
for i in lst:       # 각 중량을 i로
    target = i*N    # 각 중량별 최대 중량
    if target > max:    # 방금 구한 값이 max값보다 크다면
        max = target    # max값을 갱신시킨다.
    N -= 1          # i이상을 들 수 있는 로프 수

print(max)


'''
예제를 5 10 20 30 40 으로 이미 sort를 시킨 상태의 배열로 생각해서 문제 풀때 sort를 안 해줬더니 실패했다.
target *N을 해주고 각 중량마다 N-1을 해주려면 sort를 해주어야 한다.
'''
