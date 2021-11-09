from collections import Counter

N, M, B = map(int, input().split())

data = []
counter = Counter()

for _ in range(N):  # i가 안 쓰일 때
    row = list(map(int, input().split()))
    data.append(row)
    counter.update(row)

"""
3 4 99
0 0 0 0
0 0 0 0
0 0 0 1
입력시 Counter({0: 11, 1: 1})
"""

maximum_height = max(counter)
minimum_time = 2200000000
answer_height = 0

total = B  # 99
for i in range(257):  # 0~256
    # counter --> 11 1 0 0 0 0 ...
    # 0부터 256까지 각각의 개수
    total += counter[i] * i
    # total= 99(B)+1
bound = total // (N * M)  # 8
# bound는 인벤토리에 있는 모든 블록을 사용해서 일정한 높이를 만들 때 최대 높이

for height in range(bound + 1):  # 0~8  --> 고르게 만드는 땅의 높이
    time_spent = 0
    for current in range(257):  # counter 모두 검사
        # range(500*500)아닌가 라고 생각했지만 counter는 0~256의 층 개수를 의미하는 것
        cnt = counter[current]
        if current < height:
            time_spent += (height - current) * cnt  # 블록을 쌓는 작업
        else:
            time_spent += (current - height) * cnt * 2  # 블록을 제거하는 작업
    if minimum_time >= time_spent:
        minimum_time = time_spent
        answer_height = height

print(minimum_time, answer_height)
