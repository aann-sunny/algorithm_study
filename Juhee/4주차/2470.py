import sys

num = int(sys.stdin.readline())
feature_list = list(map(int, sys.stdin.readline().split()))
feature_list.sort()

start = 0
end = len(feature_list) - 1
ans = feature_list[start] + feature_list[end]
al = start
ar = end

# 투포인터 이용
while start < end:
    result = feature_list[start] + feature_list[end]
    if abs(ans) > abs(result):
        ans = result
        al = start
        ar = end
        if ans == 0:
            break
    if result < 0:  # 합이 음수일 경우 더 큰 음수를 더함
        start += 1  # end-=1와 헷갈렸으나 그럴 경우 절댓값은 더 커짐
    else:  # 합이 양수일 경우 더 작은 양수를 더함
        end -= 1  # start+=1와 헷갈렸으나 그럴 경우 절댓값은 더 커짐

print(feature_list[al], feature_list[ar])

# O(N)
"""
피드백 코멘트 :
투포인터를 이용해 잘 풀어주셨습니다. start를 증가시키고, end를 감소시켰을 때 어떤 영향이 있는지 잘 고민해보신 것 같습니다.
"""
