# 완료
total = int(input())
num = 0
numbers = []

for i in range(total):
    sum = 0
    num = i
    while i > 0:
        sum += i % 10
        i //= 10
    if sum + num == total:
        numbers.append(num)

if not numbers:
    print(0)
else:
    print(min(numbers))

# O(N)
