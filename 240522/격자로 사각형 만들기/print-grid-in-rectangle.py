n = int(input())

maps = [[0]*n for _ in range(n)]

for i in range(n):
    maps[0][i] = 1
    maps[i][0] = 1

for i in range(1, n):
    for j in range(1,n):
        maps[i][j] = maps[i-1][j] + maps[i][j-1] + maps[i-1][j-1]

for m in maps:
    print(*m)