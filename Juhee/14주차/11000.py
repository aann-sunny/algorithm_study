"""
1931과 비슷한 것 같다.
차이점: 모든 수업을 가능하게 해야한다.
sort를 이용해보자.
"""

import sys
import heapq

N = int(input())

# 한줄로 list에 담기
time_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
time_list.sort(key=lambda x: x[0])  # 일찍 시작 순서대로 정렬

classroom_list = []  # 종료시간
heapq.heappush(classroom_list, time_list[0][1])  # 첫 번째 강의의 종료 시간

for i in range(1, N):
    if classroom_list[0] > time_list[i][0]:  # 만약 다음 강의의 시작 시간이 더 이르다면
        heapq.heappush(classroom_list, time_list[i][1])
    else:  # 강의의 종료 시간이 더 이르다면
        heapq.heappop(classroom_list)
        heapq.heappush(classroom_list, time_list[i][1])

print(len(classroom_list))
