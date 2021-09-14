import sys

n= int(sys.stdin.readline().rstrip())
lst=[]
for i in range(n):
    put= list(map(int, input().split()))
    lst.append(put)

lst.sort(key=lambda x:[x[0],x[1]])


