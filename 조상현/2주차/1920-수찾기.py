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