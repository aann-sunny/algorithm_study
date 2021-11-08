# 완료
num = int(input())
conference_list = [[0 for col in range(2)] for row in range(num)]
num_list = list(range(num))

for i in range(num):
    start, end = map(int, input().split())
    conference_list[i][0] = start
    conference_list[i][1] = end

# conference_list = sorted(conference_list, key=lambda x: x[0])  # 일찍 시작하는 순서
# conference_list = sorted(conference_list, key=lambda x: x[1])  # 끝나는 시간이 빠른 순서
conference_list = sorted(conference_list, key=lambda x: (x[1], x[0]))

maxnum = 0
start = 0
for conference in conference_list:
    if conference[0] >= start:
        maxnum += 1
        start = conference[1]

print(maxnum)

# O(N)

"""
잘 푸셨습니다! 정렬을 2번 하고 있는데, 사실 sorted는 다중키로 정렬이 가능합니다.
key=lambda x: (x[1], x[0]) 이런식으로 원하는 우선순위를 나열하면 됩니다.
"""
