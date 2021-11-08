# 완료
import sys

sys.setrecursionlimit(10 ** 6)
n, m = map(int, sys.stdin.readline().split())
num_list = [i for i in range(n + 1)]


def find(a):
    if num_list[a] == a:
        return a
    num_list[a] = find(num_list[a])  # 재귀를 통해 같은 소속 모두 찾기
    return num_list[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        num_list[b] = a


for i in range(m):
    x, y, z = list(map(int, sys.stdin.readline().split()))
    if x == 0:
        union(y, z)
    elif x == 1:
        if find(y) == find(z):
            print("YES")
        else:
            print("NO")

# 결론적으로 같은 num_list에서 같은 숫자의 원소들의 인덱스는 같은 집합

"""
피드백 코멘트 :
분리집합을 연습해볼 수 있는 좋은 경험이 되셨을 것 같습니다.
깔끔하게 잘 풀어주신 것 같네요. 고생하셨습니다!
"""
