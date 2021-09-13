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

