import sys


class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


def pre_order(key):                     # 전위 순회(루트 > 왼쪽 자식> 오른쪽 자식)
    node = tree[key]
    print(node.value, end="")
    if node.left != '.':
        pre_order(node.left)
    if node.right != '.':
        pre_order(node.right)


def in_order(key):                      # 중위 순회(왼쪽 자식 > 루트 > 오른쪽 자식)
    node = tree[key]
    if node.left != '.':
        in_order(node.left)
    print(node.value, end="")
    if node.right != '.':
        in_order(node.right)


def post_order(key):                    # 후위 순회 (왼쪽 자식 > 오른쪽 자식 > 루트)
    node = tree[key]
    if node.left != '.':
        post_order(node.left)
    if node.right != '.':
        post_order(node.right)
    print(node.value, end="")


input = sys.stdin.readline
N = int(input())
tree = {}

for i in range(N):
    value, left, right = input().split()
    node = Node(value, left, right)
    tree[value] = node


pre_order('A')
print()

in_order('A')
print()

post_order('A')
print()
