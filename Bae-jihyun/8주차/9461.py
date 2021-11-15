
T = int(input())

for _ in range(T):
    N = int(input())
    dp = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

    for n in range(11, N+1):
        dp.append(dp[n-1]+dp[n-5])

    print(dp[N])


'''
풀이 과정 생각
그림을 보니 이전꺼 + 이전꺼 라는 반복을 느꼈다.
'''
