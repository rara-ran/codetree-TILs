def is_able():
    for _ in range(5):
        num = int(input())
        if num % 3 != 0:
            return 0
    return 1

print(is_able())