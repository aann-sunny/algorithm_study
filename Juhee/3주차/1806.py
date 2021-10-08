#피드백 후 수정

"""
3. 2번 방법과는 다르게 start 이후 조건에 맞을 때까지 모두 end를 더하지 않음 --> 시간 절약
조건에 만족할 때까지 뒤로 더하고 조건에 성립하면 앞을 빼기를 반복하여 가장 작은 값 구하기
"""

import sys
N,S =map(int,sys.stdin.readline().split())  #스페이바 공백을 기준으로 int형 변수 두개 입력받기
num_list=list(map(int,sys.stdin.readline().split()))  #N번만큼 split
i,j=0,0
result=0
ans=N+1

while True:
    if result<S:
        if j==N:break
        else:
            result+=num_list[j]
            j+=1
    else:
        result-=num_list[i]
        i+=1
        ans=min(ans,j-i+1)

if ans==N+1:
    print(0)
else:
    print(ans)

"""
1. for문 3번--> 시간 초과
선택 개수와 시작 인덱스를 기준으로 하니 불필요하게 for문을 과도하게 돌아감
N,S=map(int,input().split())  

num=input()
num_list=list(map(int,num.split(maxsplit=N)))  

def calcsum(num_list,start,count):
    sum_num=0
    for i in range(count):
        sum_num+=num_list[start+i]
    return sum_num

flag=True

for j in range(1,S+1):  #선택 개수
    for i in range(N):   #어느 인덱스부터 시작하는지
        if i+j<=N:
            if calcsum(num_list,i,j)>=S:
                print(j)
                flag=False
                break
    if flag==False:
        break

if flag==True:
    print('0')   


2. 시간 초과
1번 방법보다는 코드가 줄어들었지만 여전히 시간 초과
start를 for문을 통해 정하고 end는 인덱스 start~N까지 돌아가며 start가 갱신될 때 마다 조건에 만족할 때까지 그 뒤까지 모두 sum
import sys
N,S =map(int,sys.stdin.readline().split())  

num_list=list(map(int,sys.stdin.readline().split()))  


if sum(num_list)<S:
    print('0')
else:
    minnum=S+1
    for start in range(N):
        num_sum=0
        for end in range(start,N):
            if num_sum>=S:
                minnum=min(minnum,end-start)                    
            else:
                num_sum+=num_list[end]

    print(minnum)



피드백 코멘트 :
시간초과가 난 상황에서는 지금 작성하신 풀이의 시간복잡도가 얼마나 되는지 계산해보시면 좋습니다.
문제 조건과 비교해서 내 알고리즘이 시간내 통과할 수 있을지 가늠해보는거죠.
대략 1억번의 연산이 1초내에 통과된다고 가정하는편이니, 주희님의 알고리즘이 문제의 최대 조건에서 1억회 이상 연산하면 통과하기 어렵습니다.
시간복잡도 결과 분석에 따라 큰 비중을 차지하는 중첩문을 간소화하거나, 경우에따라 알고리즘 전체를 수정해야할 수도 있습니다.
"""