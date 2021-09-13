# 백준 2231 - 분해합(https://www.acmicpc.net/problem/2231)

# def hasContructor(N):
#     for num in range(1, N):
#         sum, num_to_str = num, str(num)
#         # for i in range(0, len(num_to_str)):
#         #     sum += int(num_to_str[i])
#         for i in num_to_str:
#             sum += int(i)
#         if sum == N:
#             return num
#     return 0

def getContructor(N):
    for num in range(1, N):
        sum, dec = num, num
        while dec:
            sum += dec % 10
            dec //= 10          
        if sum == N:
            return num
    return 0

N = int(input())
print(getContructor(N))