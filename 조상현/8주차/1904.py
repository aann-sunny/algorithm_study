"""
길이가 1인 이진수열 : 1                                                 (1개)
길이가 2인 이진수열 : 00, 11                                            (2개)
길이가 3인 이진수열 : 001, 111, 100                                     (3개)
길이가 4인 이진수열 : 0011, 1111, 1001, 0000, 1100                      (5개)
길이가 5인 이진수열 : 00111, 11111, 10011, 11001, 00100, 11100, 10000   (8개)
길이가 n인 이진수열 개수 : 길이가 n - 1인 이진수열에 1타일을 붙인 이진수열의개수(길이가  n - 1인 이진수열개수)
                    +   길이가 n - 2인 이진수열에 00타일을 붙인 이진수열의개수(길이가 n - 2인 이진수열개수)

                    >> 길이가 n - 2인 이진수열에 1타일 2개를 이어붙이는 경우는 길이가 n - 1인 이진수열에
                       1타일을 붙여서 길이가 n인 이진수열을 만드는 경우에 포함되므로 세지 않음.
"""

N = int(input())

dp = [0, 1, 2]

def solution(x):
    if x > 2:
        for i in range(3, x + 1):
            dp.append((dp[i - 1] + dp[i - 2]) % 15746)
    return dp[x]

print(solution(N))

"""
파이썬은 정수형의 최대범위?가 없는 걸로 알고 있어서 리턴할때 15746으로 나눈 값을 출력해도 문제없을거라 생각했으나
메모리 초과가 나서 중간 계산 과정에 15746으로 나누는 과정으로 바꿨다. 메모리 제한도 아예 신경을 안 쓰면 안 될 것 같다..
"""
