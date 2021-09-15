# 백준 1931 회의실 배정 (https://www.acmicpc.net/problem/1931)
import sys

discussion = []           # 각 회의들 저장할 리스트
N = int(input())          # 회의 개수 입력받기

for i in range(N):
    inputs = list(map(int, sys.stdin.readline().split()))
    discussion.append(inputs)                        # 각 회의들 입력받기

discussion.sort(key=lambda x:(x[1], x[0]))           # 각 회의들 정렬 - 1순위 : 종료시간, 2순위 : 시작시간

i, count = 0, 0                                # i : while문에서 쓰일 루프변수, count : 개수 세는 용도

e = 0                                          # e : 마지막으로 고른 회의의 종료시간

for i in range(0, len(discussion)):
    if discussion[i][1] >= e and discussion[i][0] >= e:
        count += 1
        e = discussion[i][1]

print(count)

"""
태홍님 피드백 보고 if문을 좀 더 정리해둠
if문이 여러번 쓰일 때, and나 다른 비교연산자들을 활용해서
코드를 더 짧게 써서 간결하게 표현할 수 있는지 체크하는 습관을 길러야 할 것 같다.
"""
