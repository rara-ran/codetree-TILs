a, b = map(int, input().split())

def is_able(a, b):
    for i in range(a, b+1):
        if 1920 % i == 0 and 2880 % i == 0:
            return 1
    return 0

print(is_able(a,b))