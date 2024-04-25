n = int(input())
maps = [[0]*n for _ in range(n)]
start = 1
for i in range(n):
    if i % 2 == 0:
        maps[i] = [x for x in range(start, start+n)]
        start = maps[i][-1] + 2
    else:
        maps[i] = [x for x in range(start, start+2*n, 2)]
        start = maps[i][-1] + 1

for m in maps:
    print(*m)