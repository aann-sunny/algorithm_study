N=int(input())
s=[0,1]   
#s[0]=0 --> indexoutofrange 막기 위해
#s[1]=1 -->가장 처음에 1으로 시작해야함

for i in range(2,N+1):
    s.append(s[i-2]+s[i-1])

'''
N=5일 때
0 1 0 _ _ _
뒤 세자리의 경우의 수 = s[3] + s[4]에서 맨 앞 1 뺀 것                    
'''
print(s[N])