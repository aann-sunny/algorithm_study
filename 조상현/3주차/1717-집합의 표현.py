# 백준 1717 - 집합의 표현(https://www.acmicpc.net/problem/1717)
# 참고 링크 : https://www.youtube.com/watch?v=AMByrd53PHM
"""
분리집합의 개념이 뭔지 배우고 적용하며 풀어봤다
"""



import sys
sys.setrecursionlimit(10**6) # RecursionError 방지

n, m = map(int, sys.stdin.readline().split())
parant = [i for i in range(n + 1)]          # parant 초기화 - 최초엔 0부터 n까지의 모든 애들의 부모가 자기자신인 상태
                                            # parant[a] = b라면 a의 부모가 b인 것임, 현재는 임의의 x에 대해 parant[x] = x인 상태

def getParant(x):         # x의 부모(가장 조상)를 리턴
    if parant[x] == x:    # x의 부모가 자기자신이라면 x를 그대로 리턴
        return x        
    parant[x] = getParant(parant[x])     # x의 부모가 자기자신이 아님 -> x의 부모를 제일 조상인(?) 애로
    return parant[x]                     # 결국은 x의 가장 조상인 애를 리턴 

def union(x, y):        # x가 속한 집합과 y가 속한 집합 합치기 - 가장 조상인 애들을 비교해 더 작은 쪽으로 합침
    x, y = getParant(x), getParant(y)
    if x < y:           # x가 더 작으니까 y의 부모를 x로
        parant[y] = x
    elif x > y:         # y가 더 작으니까 x의 부모를 y로
        parant[x] = y              
        """
        이렇게 하면 x가 속한 집합과 y가 속한 집합이 합쳐지는 이유
        : 부모가 같은 애들끼리 같은 집합인 것으로 표현하고 있음. parant[a] = b라면 a는 b가 이끄는 모임에 속해있다고 생각해도 됨
          이때 b의 부모(parant[b])가 c로 바뀌면, b는 c가 이끄는 모임에 속하는 것이라 볼 수 있고 자연스레 b가 이끄는 애들도 c가 이끄는 모임으로 따라옴
          이 부분이 getParant()함수에서 재귀를 통해 이뤄짐 
        """

def hasSameParant(x, y):         # x, y가 같은 부모를 같는지 즉 같은 집합에 속해있는지
    x, y = getParant(x), getParant(y)
    if x == y:
        return "YES"
    else:
        return "NO"


for i in range(m):
    c = list(map(int, sys.stdin.readline().split()))
    if c[0] == 0:
        union(c[1], c[2])
    else:
        print(hasSameParant(c[1], c[2]))