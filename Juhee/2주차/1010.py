# 완료
import math
import sys

# combinations 패키지도 사용 가능하나 단순 개수만 구하면되는 문제라 factorial 사용
# 단순 조합 문제 --> 조합 공식 사용

num = int(input())
for i in range(num):
    N, M = map(int, sys.stdin.readline().split())
    ans = math.factorial(M) // (math.factorial(N) * math.factorial(M - N))
    print(ans)

# O(N)

"""
피드백 코멘트 :
팩토리얼 내장 라이브러리를 잘 사용하셨네요! math 라이브러리에는 다른 유용한 함수가 많으니 찾아보셔도 좋을 듯 합니다.
"""
