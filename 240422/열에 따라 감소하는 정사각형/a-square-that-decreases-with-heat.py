n = int(input())
num = [x for x in range(n, 0, -1)]
for _ in range(n):
    print(*num)