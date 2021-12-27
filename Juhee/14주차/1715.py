"""
왜 틀렸지???????????????
import sys

N = int(sys.stdin.readline())
num_list = []
ans_list = []
 
for _ in range(0, N):
    num = int(sys.stdin.readline())
    num_list.append(num)

num_list.sort()

if N == 1:
    print(0)

else:
    ans = num_list[0] + num_list[1]
    ans_list.append(ans)
    if N != 2:
        for i in range(2, N):
            ans += num_list[i]
            ans_list.append(ans)
    print(sum(ans_list))
"""

# 직관적으로 작은 것 순으로 더해야 해가 가장 적음을 알 수 있음
import sys
import heapq

input = sys.stdin.readline

N = int(input())
hq = sorted([int(input()) for _ in range(N)])
ans = 0
for _ in range(N - 1):  # 반복문을 통해 두개 더하고 넣고 다시 더하고 넣고 반복
    a, b = heapq.heappop(hq), heapq.heappop(hq)  # 작은거 두개 꺼내서
    c = a + b  # 더하고
    ans += c
    heapq.heappush(hq, c)  # 다시 넣기
print(ans)
