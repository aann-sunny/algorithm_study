import math
import sys
#combinations 패키지도 사용 가능하나 단순 개수만 구하면되는 문제라 factorial 사용
#단순 조합 문제 --> 조합 공식 사용

num = int(input())
for i in range(num):
    N,M = map(int,sys.stdin.readline().split())
    ans = math.factorial(M)//(math.factorial(N)*math.factorial(M-N)) 
    print(ans)
