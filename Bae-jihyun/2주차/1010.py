# O(T) : T만큼 반복

import math

T = int(input())           # 테스트 케이스의 개수

for i in range(T):
    start, end = map(int, input().split())
    top = math.factorial(end)
    bottom = (math.factorial(end - start) * math.factorial(start))

    anwser = top // bottom
    print(anwser)

    # print(math.comb(end, start))


'''
anwser 계산 중에 /가 아닌 //로 풀기가 중요
math.comb(a,b)는 nCk와 같은 조합 값을 반환. (순서 상관 없음)
조합은 n개의 수 중 k개를 꺼내는 수와 동일.

'''
