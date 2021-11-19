n, k = map(int, input().split())  # n:물품의 수, k:버틸 수 있는 무게
lst = [[0, 0]]                    # lst: 입력받는 배열
result = [[0] * (k+1) for _ in range(n+1)]  # result: dp에 사용되는 배열

for _ in range(n):
    lst.append(list(map(int, input().split())))


for i in range(1, n+1):     # 가방에 넣어지는 물건
    w = lst[i][0]           # w:각 물건의 무게
    v = lst[i][1]           # v:각 물건의 가치
    for j in range(1, k+1):    # 가방에 넣을 수 있는 무게
        if j >= w:
            result[i][j] = max(result[i-1][j-w] + v, result[i-1][j])  # 아래 참고
        else:
            # j가 w보다 작으면 i-1번째의 j를 가져온다.
            result[i][j] = result[i-1][j]


print(result[i][j])  # 물건을 넣을 수 있는 최대 가치


'''
result[i][j] = max(lst[i][j-w] + v, lst[i-1][1])
lst[i-1][j-w]+v: 현재 물건의 가치(v)와 현재 물건을 넣고 나면 j무게에서 남는 나머지 무게의 최대
lst[i-1][1]: j무게에서 여태까지 중 제일 높은 가치

만약 j가 6이면 6키로를 넣을 자리가 있는데 w가 5키로인 물건을 가방에 넣고 싶다면, 1키로의 여유분이 남는다.
그럼 1키로일때 최대 가치인 lst[i-1][1](lst[i-1][j-w])와 현재 물건의 가치(v)를 더한다.(5키로와 1키로의 최대가치)
또는 i-1일때 j의 최대 가치(현재 물건을 추가하기 전)의 max를 구해 result[i][j]에 넣는다.


자꾸 index error가 나서 왜인지 보니까 j-w와 i-1때문에 for문의 range가 1부터여야했고
그래서 lst와 result의 배열 맨 앞에는 [0,0]과 [0,0,0,0,0]등 빈 배열이 있어야했다.
또한 lst입력받을 때 물건 한개의 무게가 가방에 넣을 수 있는 최대무게보다 크면 아예 빼고 입력받았는데
그렇게 하면 뒤에 index error가 발생한다.
'''
