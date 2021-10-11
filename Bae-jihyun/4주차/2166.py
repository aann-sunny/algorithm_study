import sys

# 입력 받기
N= int(sys.stdin.readline().rstrip())
lst=[]
a = 0
b = 0

for _ in range(N):
    lst.append(list(map(int, input().split())))

# 0 ~ N-1까지 신발끈 공식을 사용하고 
for i in range(N-1):   
    a += lst[i][0]*lst[i+1][1]
    b += lst[i][1]*lst[i+1][0]

# for문을 벗어나는 연산은 따로 실행해줌.
a = a + lst[N-1][0]*lst[0][1]
b = b + lst[N-1][1]*lst[0][0]


# 공식대로 절대값을 먼저 씌워주고 2로 나눠주고 반올림해주기. 
print(round(abs(a-b)/2,1))



'''
신발끈공식을 사용해야 한다는 것을 알게 되었다. 
신발끈 공식 : 
1/2 * | (x1*y2 + x2*y3 + .. + xn-1*yn + xn*y1) - (y1*x2 + y2*x3 + .. + yn-1*xn + yn*x1) |

abs를 round보다 먼저 실행해야 된다!  
'''