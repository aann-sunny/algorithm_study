from itertools import combinations

num = int(input())
conference_list=[[0 for col in range(2)] for row in range(num)]
num_list=list(range(num))

for i in range (num):
    start,end=map(int,input().split())
    conference_list[i][0]=start
    conference_list[i][1]=end

for i in range (1,num+1):
    print(list(combinations(num_list,i)))

