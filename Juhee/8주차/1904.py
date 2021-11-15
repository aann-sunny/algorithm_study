import sys,math

N = int(sys.stdin.readline())

dp_list=[[0] for _ in range(1000001)]
dp_list[1]=1
dp_list[2]=2
dp_list[3]=3

j=2
k=0
for i in range(4,N+1):
    dp_list[i]=dp_list[i-1]+j
    k+=1
    j+=k
    

print(dp_list[N]%15746)
