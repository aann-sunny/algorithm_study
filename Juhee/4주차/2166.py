N = int(input())
ass = [[]] * N
for i in range(N):
    ass[i] = list(map(int, input().split()))

left = 0
right = 0

for i in range(N):
    left += ass[i][0] * ass[(i + 1) % N][1]
    right += ass[i][1] * ass[(i + 1) % N][0]

print(((round(abs(left - right) / 2 * 100) // 10) / 10))

# O(N)
"""
피드백 코멘트 :
7번 라인에서 리스트의 맨 앞 내용을 복제해서 맨 뒤로 넣고 있는데요, 더 좋은 방법은 없을까요?
마지막 결과를 출력하는 부분은 조금 더 간단하게 만드는 것도 개선포인트가 될 수 있습니다. (자릿수를 지정하는 방식 등)
"""
