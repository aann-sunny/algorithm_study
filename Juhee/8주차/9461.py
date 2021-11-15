import sys

sys.setrecursionlimit(10000)

T = int(sys.stdin.readline())

sequence = [0, 1, 1, 1, 2]  # P 수열은 1부터 시작이므로 sequence[0]을 안씀

N_list = []

for _ in range(T):
    N_list.append(int(sys.stdin.readline()))

for i in range(5, max(N_list) + 1):
    sequence.append(sequence[i - 5] + sequence[i - 1])

for i in range(T):
    print(sequence[N_list[i]])
