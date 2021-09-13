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

commands = {
    'push' : push,
    'pop' : pop,
    'size' : size,
    'empty' : empty,
    'top' : top
}

N = int(input())

for i in range(0, N):
    inputs = sys.stdin.readline().split()

    if inputs[0] == "push":
        commands['push'](inputs[1])
    else:
        commands[inputs[0]]()

"""
잘 모르지만 if, elif를 통해 입력받은 값이 뭔지를 하나하나 따지면서 실행하기보다는
c언어의 switch문을 활용한 것처럼 딕셔너리에 함수들을 지정해놓고 쓰는 게 더 빠를 것 같아서 
이렇게 해봤습니다
"""
