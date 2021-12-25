'''
접근 1
문제를 읽어보니 작은 순대로 더하는 것이 더 효율적이라고 생각이 들어
여러 예제를 통해 확인해본 결과 sort를 시키고 작은 순부터 더하는 것이 맞다고 생각했다.

list의 sort는 O(N Log N)으로 N이 최대 100,000이므로 대략 1,600,000이므로 통과
하지만 heapq를 이용해 가장 작은 수를 pop함으로써 O(1)로 최적화시킴.
'''
import heapq

N = int(input())
lst = []
result = 0

for _ in range(N):
    lst.append(int(input()))

heapq.heapify(lst)      # list를 heap으로 변환. O(N). 아직 정렬되어있지 않음.

while len(lst) != 1:    # 아래에서 pop과 push가 계속 일어난다. len이 1이 되면 더이상 계산할 필요가 없음.
    num1 = heapq.heappop(lst)       # heappop : 가장 작은 원소 삭제 후 그 값 리턴
    num2 = heapq.heappop(lst)
    Sum = num1 + num2
    result += Sum
    heapq.heappush(lst, Sum)        # heappush : 힙 원소를 추가

print(result)

'''
처음에는 list를 사용해서 풀었는데 그림을 그려서 예제를 푼 것과 달리 쉽게 되지 않았다.
제일 작은 원소 두개를 합친 값과 lst의 다음 값을 더해가려면
list 속 원소들을 빼고 넣기를 자유자재로 할 수 있어야 했다.
인터넷을 찾아보니 python의 lib중 heapq라는 것을 발견했다.
heap : 항상 가장 작은 원소의 값을 0번으로 두는 자료구조이다.
'''
