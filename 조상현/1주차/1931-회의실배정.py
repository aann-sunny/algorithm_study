# 백준 1931 회의실 배정 (https://www.acmicpc.net/problem/1931)
import sys

discussion = []           # 각 회의들 저장할 리스트
N = int(input())          # 회의 개수 입력받기

for i in range(N):
    inputs = list(map(int, sys.stdin.readline().split()))
    discussion.append(inputs)                        # 각 회의들 입력받기

discussion.sort(key=lambda x:(x[1], x[0]))           # 각 회의들 정렬 - 1순위 : 종료시간, 2순위 : 시작시간

i, count = 0, 0                                # i : while문에서 쓰일 루프변수, count : 개수 세는 용도

e = 0                                          # e : 마지막으로 고른 회의의 종료시간
                            
# 마지막으로 고른 회의에서 가장 빠른 시간 내에 끝나는 회의들 골라가기
while i<len(discussion):            # 첫 회의부터 마지막 회의까지 루프돌기
    if discussion[i][1] == e:        # 만약 i번째 회의의 종료시간이 내가 마지막으로 골랐던 회의의 종료시간과 같다면
        if discussion[i][0] == e:    # 근데 그 회의의 시작시간마저 내가 마지막으로 골랐던 회의의 종료시간과 같다면 
            count += 1               # 그 회의도 진행가능하므로 count + 1
            e = discussion[i][1]
    elif discussion[i][1] > e:       # 만약 i번째 회의의 종료시간이 내가 마지막으로 골랐던 회의의 종료시간보다 크다면
        if discussion[i][0] >= e:    # 근데 그 회의의 시작시간이 내가 마지막으로 골랐던 회의의 종료시간과 같거나 크다면
            count += 1               # 그 회의는 진행가능하므로 count + 1
            e = discussion[i][1]     # 마지막으로 고른 회의는 i번째 회의가 되므로 e 재설정
    i += 1

print(count)

"""
피드백 코멘트 :
잘 푸셨습니다! 상세한 주석덕분에 이해하기 수월했어요.
if 문이 2줄씩 되어있는데, 사실 조건은 한 줄로 표현해도 괜찮습니다. 그 편이 읽기에도 더 편합니다.
그리고 if, elif 로 조건문을 두 줄로 작성하셨지만, 잘 생각해보면 한 줄로 합칠수도 있습니다.
"""
