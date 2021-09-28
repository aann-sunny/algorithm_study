# 백준 1010 - 다리놓기(https://www.acmicpc.net/problem/1010)

'''
한 사이트에는 한 개의 다리만 연결될 수 있고, 각 다리들은 서로 겹치지 않으며 N개의 다리를 만들 것이라 했기 때문에
동쪽에 있는 M개의 사이트 중 N개만 고르면 서쪽에 있는 N개의 사이트들이 순서대로 연결되는 형태라 생각해서
조합을 활용하기로 했다.

다리를 지을 수 있는 경우의 수만 구하면 된다고 해서 조합공식을 그대로 활용함(n C r = n! / ((n - r)!r!))
'''
import sys

def factorial(n):               # n!을 리턴
    answer = 1
    for i in range(1, n + 1):
        answer *= i
    return answer

def combination(n, r):          # nCr 을 리턴
    return factorial(n) // (factorial(n - r) * factorial(r))

T = int(sys.stdin.readline())
for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    print(combination(M, N))

"""
피드백 코멘트 :
팩토리얼은 파이썬 내장 라이브러리에서도 지원하니 참고해보세요! 공부 측면에서는 직접 구현해보는 경험도 필요합니다. 
실전에서는 내장 라이브러리를 쓰는 편이 나으니 익혀두시면 좋을 듯 합니다.
"""