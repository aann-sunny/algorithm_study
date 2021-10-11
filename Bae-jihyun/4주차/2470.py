import sys

# 입력받기
N = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()

# 계산에 필요한 변수
start, end = 0, N-1

# 결과 변수
a,b = 0,0   
result = float("inf")

while start < end :
    mysum= lst[start]+lst[end]
    if mysum == 0:     # 두 합이 0이면 바로 반환
        a,b=lst[start],lst[end]
        break
    
    if abs(result)>= abs(mysum):  # 지금 계산한 합(mysum)이 여태까지의 합(result)보다 작거나 같다면 
        result = mysum            # result 갱신
        a,b=lst[start],lst[end]

    if mysum < 0:     # 두 합이 음수면 sum이 더 큰 수가 되도록 start를 +1
        start +=1
    else:             # 두 합이 양수면 sum이 더 작은 수가 되도록 end를 -1
        end -=1

print(a,b)

    
'''첫번째 풀이
0과 가까우려면 절대값을 이용해야 한다고 생각했다.
sum을 구하고 sum 절댓값이 result보다 작으면 result를 갱신시킴.
투포인터로 하나하나 계산하니까 계속 시간초과

sort()를 시키고 sum이 0에 가까워지도록 s,e 배열의 가운데쪽으로 이동시켜야된다는 것을 알아냄.
'''
