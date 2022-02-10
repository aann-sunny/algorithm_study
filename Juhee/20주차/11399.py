# https://www.acmicpc.net/problem/11399
'''
앞 사람의 시간이 축적되니까 앞에 시간이 짧은 사람이 있을수록 단축할 수 있다.
그럼 sort를 하고 나서 그냥 합치면 되겠는데?
--> 그리디 알고리즘
'''
import sys

input = sys.stdin.readline

N = input()
time_list = list(map(int, input().split()))
min_time = 1000000000

time_list.sort()

'''
ans = time_list[0]

# 이중 for문은 너무 헷갈린다.
for i in range(1, len(time_list)):
    for j in range(i+1):  
        ans += time_list[j]
'''

ans = sum(time_list)

# 위 주석처리와 결과 같으나 시간이 더 적게 걸리네.
for i in range(1, len(time_list)):
    for j in range(i):
        ans += time_list[j]

print(ans)
