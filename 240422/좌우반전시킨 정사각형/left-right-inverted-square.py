n = int(input())

for i in range(1, n+1):
    num = [x*i for x in range(n, 0, -1)]
    print(*num)