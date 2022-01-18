"""
1. 열 번호가 주어지지 않는데 어떻게 알 수 있나 고민하다가 결국 검색
--> 중위 순회. 중위 순회 순서 = 열 번호
이걸 왜 생각 못했을까

2. 레벨은 어떻게 알 수 있을까

"""
import sys

input = sys.stdin.readline

num = int(input())
tree_list = []

dic = {}


class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


def in_order(key):
    node = dic[key]
    if node.left != -1:
        in_order(node.left)
    print(node.value, end="  ")  # 뿌리 print
    if node.right != -1:
        in_order(node.right)


startValue = 0
for i in range(num):
    value, left, right = map(int, input().split())
    if i == 0:
        startValue = value
    node = Node(value, left, right)
    dic[value] = node


print(in_order(startValue))


"""
중위 순회 값 출력까지 완료
아직 구현중!!!
"""
