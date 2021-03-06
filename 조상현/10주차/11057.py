"""
무식하게 풀기 : 1 ~ N자리 수까지 하나하나 오르막수인지 따짐
N의 최대 = 1000이므로 최대 10^999번 정도의 연산을 함
절대 1초내에 못 푼다

길이가 1인 오르막수 : 10개
길이가 2인 오르막수 : 길이가 1인 오르막수의 끝자리 이상인 한자리 수를
                    길이가 1인 오르막수 뒤에 붙여서 나오는 수들
길이가 3인 오르막수 : 길이가 2인 오르막수의 끝자리 이상인 한자리 수를
                    길이가 2인 오르막수 뒤에 붙여서 나오는 수들
길이가 n인 오르막수도 이런 방식으로 구함

길이가 n인 오르막수에서 마지막이 9인 오르막수 개수 = 길이가 n - 1인 오르막수에서 마지막이 9이하인 수들
길이가 n인 오르막수에서 마지막이 8인 오르막수 개수 = 길이가 n - 1인 오르막수에서 마지막이 8이하인 수들
"""

N = int(input())

def solution(x):
    # dp[i][j] = 길이가 i인 오르막수 중 끝이 j인 수의 개수
    # n은 최대 1000이므로 dp배열엔 최대 10000개의 데이터가 저장되고,
    # 10007로 나누면서 모듈러연산을 해주면 4바이트로 충분히 하나의 정수를 표현가능하므로
    # dp배열은 최대 40,000 byte 정도를 잡아먹으리라 예상함 -> 메모리 제한은 안 걸릴 듯 하다
    dp = [0, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    for i in range(1, x + 1):
        new_data = []
        for j in range(10):
            new_data.append((sum(dp[i][:j + 1]) % 10007))
        dp.append(new_data)
    return sum(dp[x]) % 10007

print(solution(N))

""" 
처음엔 30번 줄의 return쪽엔 % 10007을 안 붙이고
28번 줄에만 % 10007을 붙였는데 틀렸다고 나와서 당황했다.
알고보니 28번줄에만 모듈러 연산을 해준 경우
dp[x]의 각 값들은 모듈러 연산된 값들이지만,
sum(dp[x])는 dp[x]의 각 값들을 모두 합한 값이므로 이 값은 10007을 넘을 수도 있다.

문제의 조건에 따라 모듈러 연산을 중간에만 해주지 않고 마지막 return 전에도 경우에 따라
모듈러 연산을 해야 하는 경우가 있음을 알게 됐다
"""