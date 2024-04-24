from collections import deque

def make_rgb(color,tx,ty): # R, G, B 세가지

    dx, dy = [-1,1,0,0], [0,0,-1,1]

    q = deque()
    q.append((tx,ty))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = dx[i]+x, dy[i]+y

            if nx < 0 or ny < 0 or nx >= n or ny>=n:
                continue

            if maps[nx][ny] == color and rgb_visited[nx][ny] == 0:
                rgb_visited[nx][ny] = 1
                q.append((nx, ny))
        

def make_rg(tx,ty): # R, G 하나로
    dx, dy = [-1,1,0,0], [0,0,-1,1]

    q = deque()
    q.append((tx,ty))
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = dx[i]+x, dy[i]+y

            if nx < 0 or ny < 0 or nx >= n or ny>=n:
                continue

            if maps[nx][ny] in ('R', 'G') and rgb_visited[nx][ny] == 1:
                rgb_visited[nx][ny] = 2
                q.append((nx, ny))
        

n = int(input())
maps = [list(input()) for _ in range(n)]
rgb_visited = [[0]*n for _ in range(n)]

rgb_count, rg_count = 0, 0

for i in range(n):
    for j in range(n):
        if rgb_visited[i][j] == 0 and maps[i][j] == 'B':
            rgb_visited[i][j] = 1
            make_rgb('B', i, j)
            rgb_count+=1
            rg_count+=1

        elif rgb_visited[i][j] == 0 and maps[i][j] == 'R':
            rgb_visited[i][j] = 1
            make_rgb('R', i, j)
            rgb_count += 1
        elif rgb_visited[i][j] == 0 and maps[i][j] == 'G':
            rgb_visited[i][j] = 1
            make_rgb('G', i, j)
            rgb_count += 1


for i in range(n):
    for j in range(n):
        if rgb_visited[i][j] == 1 and maps[i][j] in ('R', 'G'):
            make_rg(i,j)
            rg_count+=1
        

print(rgb_count, rg_count)