n = int(input())

maps = [[0]*n for _ in range(n)]

num = n**2

for j in range(n):
    if j % 2 == 1:
        for i in range(n):
            maps[i][j] = num
            num -= 1
    else:
        for x in range(n-1, -1, -1):
            maps[x][j] = num
            num -= 1

for m in maps:
    print(*m)