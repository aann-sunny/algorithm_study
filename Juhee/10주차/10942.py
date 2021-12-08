# https://www.acmicpc.net/problem/10942

# 팰린드롬: 앞뒤를 뒤집어도 똑같은 문자열

import sys

"""시간 초과
N = int(sys.stdin.readline())

a_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

for _ in range(M):
    q_list = list(map(int, sys.stdin.readline().split()))
    start = q_list[0] - 1
    end = q_list[1] - 1
    while start < end:
        if a_list[start] != a_list[end]:
            print("0")  # 팰린드롬 X
            break
        start += 1
        end -= 1
    else:
        print("1")  # 팰린드롬 O
"""

"""
[start+1,end-1]이 팰린드롬이라는 사실을 이미 알고 있다면
문자열 전체를 검사할 필요 없이 앞 뒤 두 글자 start와 end만 비교해보면 된다.
-> 어떤 문자열이 팰린드롬인지 확인하려면 양 끝의 문자가 같은지를 확인하고
양 끝단을 제외한 문자열이 팰린드롬인지 확인하면 된다.
"""
N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

# 0 -> 팰린드롬 X
# 1-> 팰린드롬 O
dp_list = [[0] * (N) for _ in range(N)]
# 헷갈릴까봐 N+1로 놓고 풀었는데 더 헷갈렸다.......

for i in range(0, N):
    for start in range(N - i):
        end = start + i
        if start == end:
            dp_list[start][end] = 1
            continue
        if numbers[start] == numbers[end]:
            if start + 1 == end:
                dp_list[start][end] = 1
            elif dp_list[start + 1][end - 1] == 1:
                dp_list[start][end] = 1


for question in range(M):
    s, e = map(int, sys.stdin.readline().split())  # 이 한줄 input으로 했다고 시간 초과.
    print(dp_list[s - 1][e - 1])
    # readline 습관화
