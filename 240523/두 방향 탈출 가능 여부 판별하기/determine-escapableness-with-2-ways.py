n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
order = 1

def in_range(x, y):
    return 0 <= x and x < n and 0<= y and y < m

def can_go(x,y):

    if not in_range(x,y):
        return False

    if not maps[x][y] or visited[x][y]:
        return False
    
    return True


def dfs(x, y):
    global order

    dx, dy = [1,0], [0,1]

    for i in range(2):
        nx, ny = x+dx[i], y+dy[i]
        
        if can_go(nx, ny):
            maps[nx][ny] = order
            order += 1
            visited[nx][ny] = 1
            dfs(nx, ny)

maps[0][0] = order
order += 1
visited[0][0] = 1
dfs(0,0)

if maps[n-1][m-1] != 1:
    print(1)
else:
    print(0)