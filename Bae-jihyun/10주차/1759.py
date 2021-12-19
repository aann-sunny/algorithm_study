import sys
from itertools import combinations

L, C = map(int, input().split())
char = sys.stdin.readline().rstrip().split()
char.sort()    # 오름차순으로 만들기
result = []

for i in combinations(char, L):  # ('a','t')
    # L길이인 한 조합의 모음, 자음 수 검사하기
    vowel = 0
    for c in i:                        # 'a'
        if c in ['a', 'e', 'i', 'o', 'u']:
            vowel += 1

    # 만약 모음이 1개 이상이고 자음이 2개 이상이라면
    if vowel >= 1 and L-vowel >= 2:
        result.append("".join(i))

for r in result:
    print(r)


'''
combinations 사용법
combinations(['a', 'b', 'c'], m) : 리스트 속 원소들을 길이 m인 모든 조합으로 만들기
ex) list(combinations(['a','t','c'], 2)) =>[('a', 't'), ('a', 'c'), ('t', 'c')]
combinations는 iterable 반복할 수 있는 객체라서 list 필요없음.

join 사용법
1) 리스트를 문자열로 만들기
    "".join(['a','b','c']) => 'abc'
2) 리스트를 문자열로 합치기
    "_".join(['a','b','c']) => 'a_b_c'

'''
