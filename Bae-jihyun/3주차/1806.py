import sys

n, s = map(int, sys.stdin.readline().split())
nlist = list(map(int, sys.stdin.readline().split()))

start, end = 0, 0
shortest = n
mysum = nlist[0]


while end < n:

    if mysum < s:    # 현재 구간 합이 s보다 작으면
        end += 1     # 현재 구간의 끝점을 늘려준다
        if end < n:  # 범위 체크
            mysum += nlist[end]

    else:            # 현재 구간 합이 s보다 크거나 같을 경우
        if shortest > end-start:     # 현재까지의 최소거리보다 짧으면
            shortest = end-start+1   # 최소거리 갱신

        if start < end:              # 구간 시작점이 끝점보다 앞에 있으면
            mysum -= nlist[start]    # 구간 합에서 시작점을 빼주고
            start += 1               # 구간 시작점을 하나 늘린다
        else:                        # 구간 시작점이 끝점과 같거나 뒤에 있으면
            end += 1                 # 구간 끝점을 하나 뒤로 늘려서 end가 start뒤에 오도록 유지
            if end < n:
                mysum += nlist[end]  # 끝점을 늘려가며 부분합 추가

if shortest != n:
    print(shortest)
else:
    print(0)


'''
현재 구간 합이 s보다 크거나 같을 경우
end를 줄이고 start를 늘리면 구간 합이 s보다 적을 수 밖에 없다.
따라서 start(구간 시작점)와 end는 늘리는 방향으로 진행된다.
'''

"""
피드백 코멘트 :
flag 변수가 없어도 될 것 같습니다. flag 변수를 사용하지 않고 구현해보는건 어떨까요??
그리고 count 변수도 사용되지 않는 것 같습니다.
"""
