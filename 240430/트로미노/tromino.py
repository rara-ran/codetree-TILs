n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
answer = []

for i in range(n-1):
    mini_arr = []
    for j in range(m-1):
        mini_arr.append(maps[i][j])
        mini_arr.append(maps[i][j+1])
        mini_arr.append(maps[i+1][j])
        mini_arr.append(maps[i+1][j+1])
        mini_arr.sort()
        answer.append(sum(mini_arr[1:4]))
        mini_arr = []

for i in range(n):
    for j in range(m-2):
        answer.append(sum(maps[i][j:j+3]))    

for j in range(m):
    mini_arr = []
    for i in range(n-2):
        mini_arr.append(maps[i][j])
        mini_arr.append(maps[i+1][j])
        mini_arr.append(maps[i+2][j])
        answer.append(sum(mini_arr))
        mini_arr = []

print(max(answer))