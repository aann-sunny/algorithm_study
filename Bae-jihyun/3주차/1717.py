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

"""
피드백 코멘트 :
코드의 17~20번 라인은 필요한 부분일까요? 만약 필요하지 않다면 왜 필요하지 않고, 필요하다면 왜 필요한지도 고민해보시면 좋을 것 같습니다.
그리고 17번 라인의 주석이 잘 이해되지 않네요. 특정 idx이상이면 find가 잘 작동하지 않는다는 의미인가요??
"""