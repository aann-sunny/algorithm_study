N,S=map(int,input().split())  #스페이바 공백을 기준으로 int형 변수 두개 입력받기

num=input()
num_list=list(map(int,num.split(maxsplit=N)))   #N번만큼 split

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

#시간 초과

"""
피드백 코멘트 :
시간초과가 난 상황에서는 지금 작성하신 풀이의 시간복잡도가 얼마나 되는지 계산해보시면 좋습니다.
문제 조건과 비교해서 내 알고리즘이 시간내 통과할 수 있을지 가늠해보는거죠.
대략 1억번의 연산이 1초내에 통과된다고 가정하는편이니, 주희님의 알고리즘이 문제의 최대 조건에서 1억회 이상 연산하면 통과하기 어렵습니다.
시간복잡도 결과 분석에 따라 큰 비중을 차지하는 중첩문을 간소화하거나, 경우에따라 알고리즘 전체를 수정해야할 수도 있습니다.
"""