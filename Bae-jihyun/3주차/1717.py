import sys

n, m = map(int, sys.stdin.readline().strip().split())

graph = [i for i in range(n+1)]


# find(1)하면 x는 1-> 3-> 7로 타고 들어감. 1,3,7이 합집합임을 알 수 있음.  
def find(x):                    # graph가 [0, 3, 2, 7, 4, 5, 6, 7] 일때, find(1)은 
    while graph[x] != x:        # while 3 != 1이니까 x에 3이 들어감
        x  = graph[x]           # while 7 != 3이니까 x에 7이 들어감
    return x                    # x : 제일 끝인 합집합

def union(x,y):
    rx = find(x)
    ry = find(y)
    if rx > ry:                # 1이 idx 2 이상부터 있으면 안 된다. find함수가 제대로 작동하지 않음. 
        graph[ry] = rx
    else:
        graph[rx] =ry


for i in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    if(a==0):
        union(b,c)
    else :
        if find(b) == find(c):
            print("YES")
        else:
            print("NO")
