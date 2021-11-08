import sys

n = int(sys.stdin.readline().rstrip())   # 입력 받기
lst = []
for i in range(n):
    put = list(map(int, input().split()))
    lst.append(put)

lst.sort(key=lambda x: [x[1], x[0]])      # 각 회의 정렬 (1순위 : 종료시간, 2순위 : 시작시간)


result = [[0, 0]]                      # 결과 배열 초기화
end = result[-1][1]                    # 마지막 회의 끝나는 시간

for some in lst:
    if end <= some[0]:                 # 회의를 이미 정렬했는데 마지막 회의 시간보다 다음 회의시간이 크다면
        result.append(some)            # result 배열에 추가
        end = result[-1][1]            # 새로운 회의가 추가됐으니 마지막 회의의 끝나는시간을 재설정

print(len(result)-1)                   # 회의의 총 갯수에서 [0,0]을 빼고 회의 갯수 출력


'''
종료시간을 1순위로 지정해야한다는 점과
2
1 3
2 2 이 반례인 점으로 result에 lst[0]이 아닌 [0,0]으로 초기화되어 있어야한다는 점을 알았다.
'''
