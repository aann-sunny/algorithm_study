# https://www.acmicpc.net/problem/10942

# 팰린드롬: 앞뒤를 뒤집어도 똑같은 문자열
# 시간 초과
import sys

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
