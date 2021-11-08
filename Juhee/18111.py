from collections import Counter

N, M, B = map(int, input().split())

data = []
counter = Counter()

for _ in range(N):  # i가 안 쓰일 때
    row = list(map(int, input().split()))
    data.append(row)
    counter.update(row)

maximum_height = max(counter)
minimum_time = 2200000000
answer_height = 0

total = B
for i in range(257):
    total += counter[i] * i
bound = total // (N * M)

for height in range(bound + 1):
    time_spent = 0
    for current in range(257):
        cnt = counter[current]
        if current < height:
            time_spent += (height - current) * cnt
        else:
            time_spent += (current - height) * cnt * 2
    if minimum_time >= time_spent:
        minimum_time = time_spent
        answer_height = height

print(minimum_time, answer_height)
