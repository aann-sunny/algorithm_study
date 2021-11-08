# 완료
"""
#최종적으로 몇개의 짐을 가져갈지 모른다는 점에서 많은 고민을 한 문제.
from itertools import combinations  #조합을 이용해 볼 수 있는 패키지 

N,K=map(int,input().split())

dic={}
cb=[]
sum_list=[]
sum_num=0
for i in range (N):
    W,V=map(int,input().split())
    dic[W]=V

for i in range(1,N+1):
    cb.append(list(combinations(list(dic.keys()),i))) #가능한 모든 조합(1개~N개)

#가져가는 개수를 기준으로 loop를 돌려봄
#불필요한 시간과 메모리를 잡아먹는 것이 아닌지..?
for i in range (len(cb)):    
    if sum_num!=0:
        sum_list.append(sum_num)
    sum_num=0
    for j in range (len(cb[i])):
        a_list=list(cb[i][j])  
        if (sum(a_list)<=N):
            for k in range (len(a_list)):
                sum_num+=dic.get(a_list[k])

print(max(sum_list))

#최종적으로 몇개의 짐을 가져갈지 모른다는 점에서 많은 고민을 한 문제.
from itertools import combinations  #조합을 이용해 볼 수 있는 패키지 

N,K=map(int,input().split())

dic={}
cb=[]
sum_list=[]
sum_num=0
for i in range (N):
    W,V=map(int,input().split())
    dic[W]=V

for i in range(1,N+1):
    cb.append(list(combinations(list(dic.keys()),i))) #가능한 모든 조합(1개~N개)

#가져가는 개수를 기준으로 loop를 돌려봄
#불필요한 시간과 메모리를 잡아먹는 것이 아닌지..?
for i in range (len(cb)):    
    if sum_num!=0:
        sum_list.append(sum_num)
    sum_num=0
    for j in range (len(cb[i])):
        a_list=list(cb[i][j])  
        if (sum(a_list)<=N):
            for k in range (len(a_list)):
                sum_num+=dic.get(a_list[k])

print(max(sum_list))


combinations는 매우 유용한 라이브러리이지만, 이 문제에는 적합하지 않습니다.
이 문제는 가능한 모든 배낭 짐들의 조합을 계산하면 답을 얻을 수 있지만, 그렇게 하지 않아도 답을 얻을 수 있습니다.
Overlapping subproblems, Optimal subproblems 두 개념에 대해 공부해보시면 좋을 것 같습니다.
"""

import sys

N, K = map(int, sys.stdin.readline().split())
numbers = [[0, 0]]

for i in range(N):
    numbers.append(list(map(int, sys.stdin.readline().split())))

dp_list = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        w = numbers[i][0]
        v = numbers[i][1]
        if j >= w:
            dp_list[i][j] = max(dp_list[i - 1][j - w] + v, dp_list[i - 1][j])
        else:
            dp_list[i][j] = dp_list[i - 1][j]

print(dp_list[N][K])

# O(NK)
