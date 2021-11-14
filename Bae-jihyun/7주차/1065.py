import sys

N = int(sys.stdin.readline().rstrip())


def cal(N):
    count = 0
    standard = 0

    # 99이하는 모두 한수.
    if N <= 99:
        return N

    # 100부터는 한수인지에 대한 계산이 필요.
    for i in range(100, N+1):
        string = list(map(int, str(i)))
        standard = string[0]-string[1]   # 기준
        for k in range(2, len(string)):
            sub = string[k-1]-string[k]
            if standard != sub:
                break
            if k == (len(string)-1):
                count = count+1
    return 99 + count


print(cal(N))

'''
문제 풀이 생각과정
N이 99이하는 모두 한수이다.
세자리 이상인 수는 2자리씩 비교해준다.

str(i) : int 숫자를 str로 만들어준다.               123 => "123"
map(int,str(i)) : 문자열을 각 정수로 만들어준다.    "123" => 1, 2, 3
list() : list로 만들어준다.                          1,2,3 => [1,2,3]
'''
