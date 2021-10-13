import sys

# 입력 받기
N= int(sys.stdin.readline().rstrip())
lst=[]
a = 0
b = 0

for _ in range(N):
    lst.append(list(map(int, input().split())))

# 0 ~ N-1까지 신발끈 공식을 사용하고 
for i in range(N):   
    a += lst[i][0]*lst[(i+1)%N][1]
    b += lst[i][1]*lst[(i+1)%N][0]

# 공식대로 절대값을 먼저 씌워주고 2로 나눠주고 반올림해주기. 
print(round(abs(a-b)/2,1))


'''
신발끈공식을 사용해야 한다는 것을 알게 되었다. 
신발끈 공식 : 
1/2 * | (x1*y2 + x2*y3 + .. + xn-1*yn + xn*y1) - (y1*x2 + y2*x3 + .. + yn-1*xn + yn*x1) |

abs를 round보다 먼저 실행해야 된다!  
'''

"""
피드백 코멘트 :
벡터의 외적을 활용한 다각형 면적 계산 방법을 사용하셨네요. 신발끈 공식이라는 이름이 있는지는 덕분에 알게 되었어요.
for문을 벗어나는 부분을 따로 처리 하셨는데요, (18~19라인) 14~15라인의 for문 내부로 넣을 수 있으니 고민해보시면 좋을 것 같네요.
"""