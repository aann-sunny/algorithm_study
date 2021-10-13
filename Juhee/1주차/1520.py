a, b = map(int, input().split())

numbers = []
for i in range(a):
    num = input()
    num_list = list(map(int, num.split(maxsplit=b)))
    numbers.append(num_list)

startnum = numbers[0][0]
