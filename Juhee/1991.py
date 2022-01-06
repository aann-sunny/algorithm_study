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


def pre_order(key):
    node = dic[key]
    print(node.value, end="")
    if node.left != ".":
        pre_order(node.left)
    if node.right != ".":
        pre_order(node.right)


def in_order(key):
    node = dic[key]
    if node.left != ".":
        in_order(node.left)
    print(node.value, end="")
    if node.right != ".":
        in_order(node.right)


def post_order(key):
    node = dic[key]
    if node.left != ".":
        post_order(node.left)
    if node.right != ".":
        post_order(node.right)
    print(node.value, end="")


pre_order("A")
print()
in_order("A")
print()
post_order("A")
