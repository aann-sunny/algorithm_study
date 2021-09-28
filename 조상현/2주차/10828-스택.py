# 백준 10828 - 스택(https://www.acmicpc.net/problem/10828)

import sys

arr = []

def push(num):
    arr.append(num)
def pop():
    print(arr.pop() if arr else -1)
def size():
    print(len(arr))
def empty():
    print(0 if arr else 1)
def top():
    print(arr[-1] if arr else -1)

N = int(input())

for i in range(0, N):
    inputs = sys.stdin.readline().split()

    if inputs[0] == "push":
        push(inputs[1])
    elif inputs[0] == "pop":
        pop()
    elif inputs[0] == "size":
        size()
    elif inputs[0] == "empty":
        empty()
    elif inputs[0] == 'top':
        top()

"""
피드백 코멘트 : 
저번에 푸신 스택 문제와 유사해서 큰 어려움은 없으셨을 것 같습니다!
"""