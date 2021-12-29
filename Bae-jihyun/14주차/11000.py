'''
접근1 : 완전탐색
S나 T가 될 수 있는 최대 10^9 크기인 배열을 만들어 그 안에 0으로 강의실 갯수를 채워준다.
Si와 Ti을 인덱스로 삼아 Si부터 Ti까지의 구간에 +1을 해주며 겹치는 시간마다 강의실 +1을 해준다.
for i in lst:
     for j in range(Ti-Si):
        result[] 채우기

lst의 길이인 N : 200,000, Ti : 10^9, Si : 1이면
시간복잡도는 200,000 * (10^9 - 1) 으로 탈락


접근2 : greedy
비슷하게 회의실 배정문제를 풀었기 때문에 일단 sort가 필요해보인다.
첫번째 강의 끝나는 시간보다 두번째 강의 시작시간이 빠르면 새로운 강의실을 배정.
첫번째 강의 끝나는 시간보다 두번째 강의 시작시간이 늦으면, 이전 강의실 이어서 쓰기.

sort는 O(N Log N)인데 N:200,000이므로 통과가능
for문도 N번 돌기때문에 충분히 통과 할 수 있다.
'''
import sys
import heapq

input = sys.stdin.readline
N = int(input())
lst = []

for i in range(N):
    lst.append(list(map(int, input().split())))

lst.sort(key=lambda x: x[0])   # 각 강의 시작시간 정렬

result = []
heapq.heappush(result, lst[0][1])      # 첫 번째 강의 끝나는 시간을 넣어줌.

for i in range(1, N):          # sort후 두번째 강의시간부터 비교
    if lst[i][0] < result[0]:  # 현재 강의실 끝나는 시간보다 다음 강의 시작시간이 빠르면
        heapq.heappush(result, lst[i][1])  # 새로운 강의실 배정
    else:                      # 현재 강의실에 이어서 강의 개최 가능
        heapq.heappop(result)  # 새로운 강의로 시간 변경을 위해 기준 시간 pop
        heapq.heappush(result, lst[i][1])  # 새 기준 시간 push

print(len(result))


'''
1 3
2 4
3 5
원래 result는 정수로 뒀는데 새 강의실을 배정하는 기준시간인 3을 기억해야하기 때문에 list로 바꿔줬다.
그 후 강의실의 갯수를 len(result)로 하기위해 pop과 push가 자유로운 heapq를 사용해봤다.
heapq의 가장 작은 원소를 0번째 인덱스로 두는 장점덕분에 기준시간을 알아서 찾아주는게 편리했다.

시간복잡도 계산을 했을때는 분명히 통과 할 수 있었는데 시간초과로 통과하지 못했다.
설마설마..? 하는 마음에 input 방법을 바꿔줬더니 눈에 띄게 빨랐다..!
'''
