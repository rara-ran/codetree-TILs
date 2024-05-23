n = int(input())

maps = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

def can_go(x,y):

    if not in_range(x,y):
        return False

    if visited[x][y] or maps[x][y] == 0:
        return False
    
    return True

def dfs(x,y):
    global order
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]

        if can_go(nx,ny):
            visited[nx][ny] = 1
            maps[nx][ny] = 0
            order += 1
            dfs(nx, ny)

answer = []

for i in range(n):
    for j in range(n):
        order = 1
        if maps[i][j]:
            visited[i][j] = 1
            dfs(i,j)
            answer.append(order)
            

answer.sort()
print(len(answer))
for a in answer:
    print(a)