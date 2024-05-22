maps = [list(map(int, input().split())) for _ in range(4)]
answer = 0

for i in range(1, 5):
    for j in range(i):
        answer+=maps[i-1][j]

print(answer)