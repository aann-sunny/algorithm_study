"""
트리 문제는 개념은 알겠는데 문제를 풀면 너무너무 어렵다!!!

1. 1991처럼 노드 클래스 만들어서 풀기
이진트리를 만들고 이를 다시 후위 순회 해보자
전위 순회(preorder): 루트 -> 왼쪽 -> 오른쪽
후위 순회(postorder): 왼쪽 -> 오른쪽 -> 루트
-> 시간 초과 오류

2. https://backtony.github.io/algorithm/2021-02-18-algorithm-boj-class4-20/

"""

import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

pre_order = []


def postOrder(start, end):
    if start > end:
        return
    root = pre_order[start]
    idx = start + 1

    while idx <= end:
        if pre_order[idx] > root:
            break
        idx += 1

    postOrder(start + 1, idx - 1)  # 왼쪽 서브트리
    postOrder(idx, end)  # 오른쪽 서브트리
    print(root)  # 후위순회이므로 마지막에 root print


while True:
    try:
        pre_order.append(int(input()))
    except:
        break

postOrder(0, len(pre_order) - 1)
