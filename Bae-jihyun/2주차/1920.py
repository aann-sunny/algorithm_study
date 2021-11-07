N = int(input())
A = list(map(int, input().split()))
A.sort()

M = int(input())
B = list(map(int, input().split()))


def calc(i):
    mid = len(A)//2
    left = 0
    right = len(A)-1
    while (left <= right):
        if(i < A[mid]):
            right = mid-1
        elif(i > A[mid]):
            left = mid+1
        elif (i == A[mid]):
            left = 0                  # 초기화
            right = len(A)-1
            mid = len(A)//2
            return 1                # 찾으면 1 반환
        mid = (left+right)//2
    return 0                        # 못 찾으면 0 반환


for i in B:
    print(calc(i))
