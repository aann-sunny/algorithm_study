"""
    A
   / \
  B   C
 /   / \
D   E   F
         \
          G

A B C
B D .
C E F
E . .
F . G
D . .
G . .
"""


class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


N = int(input())
dic = {}

for _ in range(N):
    value, left, right = input().split()
    node = Node(value, left, right)
    dic[value] = node


"""
전위 순회: 뿌리 -> 왼쪽 자식 -> 오른쪽 자식
중위 순회: 왼쪽 자식 -> 뿌리 -> 오른쪽 자식
후위 순회: 왼쪽 자식 -> 오른쪽 자식 -> 뿌리
"""


# 뿌리 -> 왼 -> 오
def pre_order(key):
    node = dic[key]
    print(node.value, end="")  # 뿌리 print
    # 왼쪽 먼저 진행이므로 left 이후 right
    if node.left != ".":
        pre_order(node.left)
    if node.right != ".":
        pre_order(node.right)


# 왼 -> 뿌리 -> 오
def in_order(key):
    node = dic[key]
    if node.left != ".":
        in_order(node.left)
    print(node.value, end="")  # 뿌리 print
    if node.right != ".":
        in_order(node.right)


# 왼 -> 오 -> 뿌리
def post_order(key):
    node = dic[key]
    if node.left != ".":
        post_order(node.left)
    if node.right != ".":
        post_order(node.right)
    print(node.value, end="")  # 뿌리 print


pre_order("A")
print()
in_order("A")
print()
post_order("A")
