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