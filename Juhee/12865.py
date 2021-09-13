from itertools import combinations

N,K=map(int,input().split())

dic={}
cb=[]
sum_list=[]
sum_num=0
for i in range (N):
    W,V=map(int,input().split())
    dic[W]=V

for i in range(1,N+1):
    cb.append(list(combinations(list(dic.keys()),i)))

for i in range (len(cb)):
    if sum_num!=0:
        sum_list.append(sum_num)
    sum_num=0
    for j in range (len(cb[i])):
        a_list=list(cb[i][j])   #조합 결정
        if (sum(a_list)<=N):
            for k in range (len(a_list)):
                sum_num+=dic.get(a_list[k])

print(max(sum_list))

