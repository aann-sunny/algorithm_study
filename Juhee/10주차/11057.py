# https://www.acmicpc.net/problem/11057

import sys

N = int(sys.stdin.readline())

"""
시간초과..........
ans = 0
for i in range(10 ** N):  # 0~10의 N승-1(9,99,999)
    num_list=list(map(int, str(i)))
    if len(num_list)==1:
        ans+=1
    else:
        start=0
        end=0
        while(end<len(num_list)-1): 
            end+=1
            if num_list[start]>num_list[end]:
                break
            else:
                start+=1
            if end==len(num_list)-1:  #모두 비교하고도 break 안 됐을 때
                ans+=1
print(ans%10007)
"""

"""
자신보다 작은 n의 값을 더해서 사용.
n/숫자 끝  0  1  2  3  4  5  6  7  8  9
        1  1  1  1  1  1  1  1  1  1  1
        2  1  2  3  4  5  6  7  8  9  10
        3  1  2  6  10  ...
6 = 3(n=2,숫자 끝=2) + 3(112,122,222)
10 = 4 + 6(113,123,133,223,233,333)
-> n 하나 위에서 0~숫자 끝까지의 합
"""

# dp_list = [[0] * 10 for _ in range(N+1)]
# 처음에는 1로 설정해두어야 함.

dp_list = list([[1] * 10])

for _ in range(N):
    dp_list.append(list([0] * 10))

for i in range(1, N + 1):  # 1~N
    for j in range(0, 10):
        for col in range(j + 1):  # 0~j
            dp_list[i][j] += dp_list[i - 1][col]

print(dp_list[N][9] % 10007)
