N=int(input())

arr=[]

for i in range(N):
    total=0
    total=sum(list(map(int, str(i))),i) # 아래 참고
    if(total==N):                       # 계산 후 N과 값이 같을 때
        arr.append(i)                   # 생성자를 array에 저장해둔다.


if len(arr)==0:         #생성자가 없을경우
    print("0")          #0을 출력
else:                   #생성자가 
    print(min(arr))     #제일 작은 생성자 출력(생성자가 여러개 일 수도 있기 때문)


#str(i) : int 숫자를 str로 만들어준다.               123 => "123"
#map(int,str(i)) : 문자열을 각 정수로 만들어준다.    "123" => 1, 2, 3
#list() : list로 만들어준다.                          1,2,3 => [1,2,3]
#sum([a],b) : 배열 a의 합과 b를 더한다.              ([1,2,3],5)=> 1+2+3+5=11
