from itertools import permutations


def calculate(x):
    ret = 0
    for i in range(len(x) - 1):
        ret += abs(x[i] - x[i + 1])
    return ret


def main():
    N = int(input())
    data = list(map(int, input().split(maxsplit=N)))
    answer = -1
    for case in permutations(data):
        answer = max(answer, calculate(case))
    print(answer)


if __name__ == "__main__":
    main()
