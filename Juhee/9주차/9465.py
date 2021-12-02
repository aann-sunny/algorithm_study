import sys

T=int(sys.stdin.readline())

for _ in range(T):
    n=int(sys.stdin.readline())
    s_list=[]
    for i in range (2):
        s_list.append(list(map(int, sys.stdin.readline().split())))
        s_list[i].insert(0,0)  #indexoutofrange 방지
    for j in range(2,n+1):
        s_list[0][j]+=max(s_list[1][j-1],s_list[1][j-2])
        s_list[1][j]+=max(s_list[0][j-1],s_list[0][j-2])
    print(max(s_list[0][n], s_list[1][n]))

 #값을 차곡차곡 더하여 최종적으로 가장 마지막 두개 원소 중 큰 것이 답       
        

