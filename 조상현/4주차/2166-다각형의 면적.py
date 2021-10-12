# 백준 2166 - 다각형의 면적(https://www.acmicpc.net/problem/2166)
"""
참고링크 : https://ko.wikihow.com/%EB%8B%A4%EA%B0%81%ED%98%95-%EB%84%93%EC%9D%B4-%EA%B5%AC%ED%95%98%EA%B8%B0
신발끈 공식을 이용해 품.
"""

import sys

N = int(sys.stdin.readline())
dot = []

for i in range(N):
    dot.append(list(map(int, sys.stdin.readline().split())))
dot.append(dot[0])

sum1, sum2 = 0, 0
for i in range(1, N + 1):
    sum1 += (dot[i][1] * dot[i - 1][0])
    sum2 += (dot[i][0] * dot[i - 1][1])

print(round(abs(sum1 - sum2) / 2, 1))
# round(a, n) : a를 소수점 n번째까지만 표현, 이 때 n+1번째 자리에서 반올림함

"""
피드백 코멘트 :
14번 라인에서 가장 첫번째 요소를 리스트의 마지막에 넣어주지 않더라도 계산할 수 있으니 개선해보시면 좋을 듯 합니다.
"""