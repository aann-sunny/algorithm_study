import sys

N=int(sys.stdin.readline())
A=set(map(int,sys.stdin.readline().split()))  #list 사용할 시 시간 초과 --> set
#list vs set --> list: 순서 O set: 순서 X
#set이 list보다 시간 복잡도 면에서 효율적

M=int(sys.stdin.readline())
B=list(map(int,sys.stdin.readline().split()))

for i in B:
    if i in A:
        print(1)
    else:
        print(0)

"""
피드백 코멘트 :
이 문제는 이분탐색으로 풀 수도 있으니, 이분탐색으로도 복습해보시면 좋을 것 같습니다!
"""