n, m = map(int, input().split())

before = [list(map(int, input().split())) for _ in range(n)]
after = [list(map(int, input().split())) for _ in range(n)]
new_maps = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if before[i][j] != after[i][j]:
            new_maps[i][j] = 1

for m in new_maps:
    print(*m)