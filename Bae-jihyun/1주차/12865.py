n, k = input().split()  
n = int(n)   
k = int(k)

table =[0]*(k+1)   #0부터 k까지의 table 생성해야해서 k+1
for i in range(n):
    w,v = [int(x) for x in input().split()]  #입력받기
    if w>k:                                  #w가 table 범위(k)넘어서면 j=0일때도 계산 안되도록 continue실행
        continue 
    for j in range(k,0,-1):                  #k부터 1까지
        if j+w <= k and table[j]!=0:         #j+w가 range안에 들어오거나, 이미 어떤 값을 가지고있으면 계산해줌
            table[j+w] = max(table[j+w], table[j]+v) #큰 값을 누적시켜야함.(큰 값을 구하고있기 때문에)
    table[w]=max(table[w],v)                 #어떤 값을 가지고 있지 않다면(j=0) 가치(v) 넣어줌. (위 식이 j=0일때와 동일)
print(max(table))



# n:3, w:3, v:6, k:7, j:4일때 
# table[7]=max(table[7], 8+6)    (table[7]=0일 때)
# 따라서 table[7]에는 14가 들어감.

"""
피드백 코멘트 :
일반적인 DP 방법론을 쓰신게 아니라 감으로 푸신 것 같은데 센스가 좋으시네요.
입력을 다 받지 않고 받을때마다 처리하신 부분, 2차원 배열이 아니라 1차원 배열로만 문제를 해결하신 점 등...
매우 효율적으로 잘 푸신 것 같습니다. 수고 많으셨습니다!
"""