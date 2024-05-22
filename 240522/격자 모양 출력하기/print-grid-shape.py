n, m = map(int, input().split())

maps = [[0]*n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    maps[a-1][b-1] = a*b

for m in maps:
    print(*m)