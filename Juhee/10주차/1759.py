# https://www.acmicpc.net/problem/1759

import sys
from itertools import combinations

L, C = map(int, sys.stdin.readline().split())
alph_list = list(map(str, sys.stdin.readline().split()))

alph_list.sort()  # 문자열도 sort 가능

# stable sort: 중복된 키를 순서대로 정렬. 순서가 중요할 때.
# unstable sort: ex)quick sort

result = []
vowels = ["a", "e", "i", "o", "u"]

# sort하고 나서 combination하기 때문에 순서 고려 더 이상 X
for c in combinations(alph_list, L):  # L개 만큼 뽑기
    vowel_count = 0
    for char in c:
        if char in vowels:
            vowel_count += 1
    if vowel_count >= 1 and L - vowel_count >= 2:  # 모음 1개 이상, 자음 2개 이상
        result.append("".join(c))  # join: 아무런 구분자 없이 하나의 string으로 변환

for r in result:
    print(r)
