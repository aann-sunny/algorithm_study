import sys

N = int(sys.stdin.readline())

dp_list = [0] * 1000001
dp_list[1] = 1
dp_list[2] = 2

for i in range(3, N + 1):
    dp_list[i] = (dp_list[i - 1] + dp_list[i - 2]) % 15746

print(dp_list[N])  # dp_list[N]%15746 --> 메모리 부족
