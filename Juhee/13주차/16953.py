"""
그리디를 해야할지 DP를 해야할지 생각해보자

가능한 연산에서 규칙이 보인다.
1. 2 곱하기 -> 1의 자리 수: 2 4 8 6
2. 1 추가 -> 1의 자리 수: 무조건 1
A가 무슨 수든 B가 홀수가 되려면 1 추가 필수
--> Greedy. 답 찾으면 바로바로

문제: 1을 중간에 추가할 경우를 고려 안함
가장 어려웠던 문제
-> 찾아보니 B에서 A로 반대로 거슬러가보라고 한다.
"""

import sys

A, B = map(int, sys.stdin.readline().split())

count = 1  # 최종 답은 최소값+1. 미리 더해주기
while True:
    if A == B:
        break
    elif A > B or (B % 10 != 1 and B % 2 != 0):
        count = -1
        break
    elif B % 10 == 1:
        B //= 10  # 뒤에 1 떼기
        count += 1
    elif B % 2 == 0:
        B //= 2
        count += 1

print(count)
