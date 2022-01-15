'''
15주차 > 1991번처럼 preorder로 트리를 생성하고 postOrder를 실행해주면 시간초과난다..
따라서 이진검색트리임을 이용해야한다.
이진검색트리 조건 : root를 기준으로 왼쪽은 root보다 값이 작고 오른쪽은 root보다 값이 크다.
'''

import sys
sys.setrecursionlimit(10 ** 6)


def postOrder(start, end):
    if start > end:
        return

    root = preOrder[start]
    idx = start + 1

    # 이진 검색 트리 조건을 이용해 서브트리 범위찾기
    while idx <= end:
        if preOrder[idx] > root:
            break
        idx += 1

    # 왼쪽 자식 순회
    postOrder(start+1, idx-1)

    # 오른쪽 자식 순회
    postOrder(idx, end)

    print(root)


preOrder = []
while True:
    try:
        preOrder.append(int(sys.stdin.readline()))
    except Exception:
        break
postOrder(0, len(preOrder) - 1)


'''
첫 입력으로 노드의 수를 받지 않으니 try except를 사용하기까지도 생각을 많이 헀다.
사용하고 나서도 except를 사용하면 안된다는 PEP8 경고 문구가 떠서 당황했다.
이 이유는 except가 BaseExceeption과 같으느 기능을 수행하는데
    이때 Ctrl+C로 종료할 수 없고 어떤 오류가 발생했는지 파악하기 어렵다는 문제가 있다.

=> try, except를 이용한 파이썬 예외 처리는 되도록 예상되는 오류를 명시해 주는 편이 좋으며,
    종류에 상관 없이 잡아내고 싶다면 except Exception: 의 형태로 작성하자.
'''
