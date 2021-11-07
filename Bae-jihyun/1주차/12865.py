import sys

n, k = map(int, sys.stdin.readline().strip().split())   # n:입력받을 횟수 , k: 최대 무게

# 0부터 k까지의 table 생성해야해서 k+1
table = [0]*(k+1)               # table: 각 무게 별 넣을 수 있는 물건들의 가치 합

for i in range(n):
    w, v = [int(x) for x in input().split()]  # 각 물건의 w: 무게, v: 가치 입력받기
    if w > k:                   # w가 table 범위(k)넘어서면 i=0일때도 계산 안되도록 continue실행
        continue

    # for문은 입력으로 들어온 v와 무게 i에 들어갈 수 있는 물건들의 가치 합을 더해주는 역할.
    for i in range(k, 0, -1):                 # k부터 1까지, i : table의 각 무게
        # i+w가 최대 무게 안에 들어오거나, 이미 어떤 값을 가지고 있으면 계산해줌
        if i+w <= k and table[i] != 0:

            # 큰 값을 누적시켜야함.(큰 값을 구하고있기 때문에)
            table[i+w] = max(table[i+w], table[i]+v)

        # print(i, table)
    # 어떤 값을 가지고 있지 않다면(i=0) 가치(v) 넣어줌. (이 식은 i=0일때와 동일)
    table[w] = max(table[w], v)
print(max(table))


"""
피드백 코멘트 :
일반적인 DP 방법론을 쓰신게 아니라 감으로 푸신 것 같은데 센스가 좋으시네요.
입력을 다 받지 않고 받을때마다 처리하신 부분, 2차원 배열이 아니라 1차원 배열로만 문제를 해결하신 점 등...
매우 효율적으로 잘 푸신 것 같습니다. 수고 많으셨습니다!
"""
