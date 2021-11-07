import sys

N = int(sys.stdin.readline().rstrip())


def cal(N):
    count = 0

    # 99이하는 모두 한수.
    if N <= 99:
        return N

    # 1000은 999와 계산 값이 같다.
    if N == 1000:
        N = 999

    # 100부터는 한수인지에 대한 계산이 필요.
    for i in range(100, N+1):
        a1, a2, a3 = list(map(int, str(i)))
        if a1 + a3 == 2 * a2:
            count = count+1
    return 99 + count


print(cal(N))

'''
문제 풀이 생각과정
N이 99이하는 모두 한수이다.
세자리 수면 등차수열의 조건인 a1+a3=2*a2 이용하여 계산해야 한다.
네자리 수이며 문제 제한으로 최대 입력인 1000은 한수가 아니기 때문에 999와 계산값이 같다.

str(i) : int 숫자를 str로 만들어준다.               123 => "123"
map(int,str(i)) : 문자열을 각 정수로 만들어준다.    "123" => 1, 2, 3
list() : list로 만들어준다.                          1,2,3 => [1,2,3]
'''


# 1000을 더 깔끔하게 처리하는 방법이 있을까요..?
