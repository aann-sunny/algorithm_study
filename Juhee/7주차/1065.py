# 삼중 for문을 이용해서 시간 복잡도를 걱정했으나 성공
# 최적화 풀이보니 불필요한 for문과 if문이 많은듯,,,,--> while문으로 고쳐보기

import sys

N = int(sys.stdin.readline())
num_list = []
anw = 0

for i in range(1, N + 1):
    for j in str(i):
        num_list.append(int(j))
    if len(num_list) < 3:  # 한자리, 두자리는 무조건 한수
        anw += 1
        num_list.clear()
    else:
        sub = num_list[1] - num_list[0]  # 맨 앞 두 자리 기준으로
        for k in range(2, len(num_list)):
            if sub != num_list[k] - num_list[k - 1]:  # 값이 다르다면 break하여 다음 숫자로
                num_list.clear()
                break
            if k == len(num_list) - 1:  # 맨 마지막까지 일치했다면 한수
                anw += 1
print(anw)
