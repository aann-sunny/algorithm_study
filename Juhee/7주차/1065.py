import sys

N = int(sys.stdin.readline())
num_list = []
anw = 0

for i in range(1, N + 1):
    for j in str(i):
        num_list.append(int(j))
    if len(num_list) < 3:
        anw += 1
        num_list.clear()
    else:
        sub = num_list[1] - num_list[0]
        for k in range(2, len(num_list)):
            if sub != num_list[k] - num_list[k - 1]:
                num_list.clear()
                break
            if k == len(num_list) - 1:
                anw += 1
print(anw)
