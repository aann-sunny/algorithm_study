'''
brute force(막무가내로 풀기)인 일일히 비교하며 중첩 for문으로 찾으면 시간초과.
보자마자 sort를 해야겠구나 생각이 들었는데
sort하면 보통 greedy라고 배웠기때문에 greedy로 풀기.

greedy : sort 후 현재 값 중 최선의 선택을 하며 O(n)이 되도록 풀기!

요점!
※ 서류점수가 나쁘면 다른 지원자보다 면접 점수가 좋아야 합격
= 더 좋은 서류점수를 가진 지원자보다 면접 점수가 높은 지원자를 뽑기
'''

import sys

T = int(input())   # 테스트 케이스 수

for _ in range(T):
    N = int(input())  # 지원자 수
    lst = []
    result = 1      # result : 합격자, sort 후 맨 앞에 오는 지원자는 서류 점수가 제일 높으니 이미 합격

    # 입력받기
    for _ in range(N):
        a = list(map(int, sys.stdin.readline().split()))
        lst.append(a)

    # 서류 심사 기준으로 정렬
    lst.sort()

    # 비교하기 (greedy하게 비교하기)
    target = lst[0][1]            # target : 합격자 중 가장 높은 면접등수
    for i in range(1, N):
        if target > lst[i][1]:    # lst[i][1]: 현재 지원자의 면접 등수
            result += 1           # 합격자 추가
            target = lst[i][1]

    print(result)

'''
if target > lst[i][1]:    # 현재 면접점수 중 가장 높은 성적보다 높으면 (등수라서 작으면으로, 부등호 > 이렇게 표시)
    result += 1           # (서류점수는 더 낮아도 면접 점수가 더 높아서) 현재 지원자는 합격
'''
