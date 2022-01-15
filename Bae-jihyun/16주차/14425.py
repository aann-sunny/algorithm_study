'''
set, dict는 Hash 값을 이용하기 때문에 검색할 때 O(1)이 걸린다.
문제를 보고 트리로 푸는 방법을 모르겠어서 일단 search하면 dict 라고 생각했기 때문에 dict를 이용했다.
Trie를 공부하기 위한 문제같아서 Trie에 관한 정리를 아래에 해두었다.
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
result = 0
dict = dict()

# 입력받기
for i in range(N):
    key = input().strip()
    dict[key] = True   # 이 부분을 True 말고 다른 것으로 둔다면 뭐가 있을까요..?

# 비교하기
for j in range(M):
    check = input().strip()
    if check in dict:
        result += 1

# 답 출력
print(result)


'''
Trie란?
- class와 dict를 이용해 노드를 만드는 자료구조
- Node :
    key(문자1개) : None,
    Data(만약 문자열이 끝났다면 끝남을 표시하기 위한 문자열전체) : None,
    child(자식 노드들) : {}    # dict 사용

    class Node(object):
        def __init__(self, key, data=None):
            self.key = key
            self.data = data
            self.children = {}
- 각 노드별 삽입(insert)와 검색(search) 함수를 만든다.

참고자료
https://youseop.github.io/2020-11-09-BAEKJOON-14425_%EB%AC%B8%EC%9E%90%EC%97%B4%EC%A7%91%ED%95%A9/
'''
