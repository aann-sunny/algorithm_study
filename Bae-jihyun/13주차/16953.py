'''
전의 값에 이런 저런 연산을 하며 누적하기 때문에 dp일 것 같다.

x2    |  2  4  8  16  32  64
r(+1) | 21 41 81  161 321 641
x2    | 42 82 162(정답)

dp 2차원 배열을 만들어 값을 누적하며 연산 두가지를 번갈아가며 실행.
-> 연산순서가 꼭 두가지를 번갈아가며 실행시키는 것이 아님. (*실패*)

※ 요점!
A -> B문제를 B-> A로.
B의 맨 끝에 1이 있다면 2로 나눌 수 없다. = 맨 끝의 1을 떼준다.
    맨 끝에 1이 아니고 2로 나누어진다. = 2로 나누어준다.

더이상 연산을 할 수 없을때까지 진행하고 B가 A와 같아지면 정답출력.
'''

A, B = map(int, input().split())

result = 0
while B > A:
    if B % 10 == 1:     # 10으로 나눴을 때 나머지가 1이면(맨 끝에 1이 있는 수라면)
        B //= 10        # 정수만 취하기
    elif B % 2 == 0:    # 2로 나눴을 때 나머지가 0이면(2로 나누어진다면)
        B /= 2          # 2로 나눠주기
    else:               # 위의 연산이 모두 안 된다면
        break
    result += 1

print(result + 1 if A == B else -1)
