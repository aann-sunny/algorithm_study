# 백준 1920 - 수 찾기(https://www.acmicpc.net/problem/1920)
import sys

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
A.sort()

M = int(input())
numbers = list(map(int, sys.stdin.readline().split()))

for target in numbers:
    left, right = 0, N - 1
    result = 0
    while(left<=right):
        mid = (left + right) // 2
        if A[mid] == target:
            result = 1
            break
        elif A[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    print(result)

"""
피드백 코멘트 :
정석적인 이분탐색으로 잘 푸신 것 같습니다!
참고로 파이썬에서는 괄호 생략이 가능해서 while left <= right 로 쓰는 것도 가능합니다.

"""