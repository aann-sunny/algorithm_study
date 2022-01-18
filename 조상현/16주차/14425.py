# M개의 문자열들과 N개의 문자열(S)들이 주어진다
# M개의 문자열들 중 S에 있는 애들의 수?

# 1. 단순히 배열에 넣어서 하기
# ==의 시간복잡도는 O(n)이므로 최악의 경우
# 10,000 * 10,000 * 500번의 연산 -> 시간초과

# 2. 배열 말고 딕셔너리로 한다면?
# in을 활용하면 시간복잡도가 O(1)으로 줄어드므로 시간단축이 가능할 것 같다

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

dict = {}

for _ in range(N):
    dict[input()] = ''

count = 0

for _ in range(M):
    keyword = input()
    if keyword in dict:
        count += 1

print(count)


# 문자열을 트리에서 활용 가능하다길래 다른 방법을 알아봤는데,
# Trie라는 자료구조가 있었다.
# ABC, ABD, AEF라는 문자열이 있을 때 트리처럼 
#     A
#    / \
#   B   E
#  / \   \
# C   D   F
# 처럼 표현한다. 
# 길이가 s인 문자열이 k개 있을 때, 특정 문자열이 있는지 확인하려면
# 리스트의 경우 sk번만큼의 연산을 해야 할 수 있으나
# 위 Trie구조?로 하면 s번만큼의 연산만 하면 됨
# 참고링크 : https://jcsoohwancho.github.io/2019-11-03-%EB%AC%B8%EC%9E%90%EC%97%B4-%EA%B2%80%EC%83%89(2)-Trie/
