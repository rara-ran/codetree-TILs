from collections import deque

maps = [list(input()) for _ in range(10)]
visited = [[0]*10 for _ in range(10)]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

start, end, nomap = 0, 0, 0

for i in range(10):
    for j in range(10):
        if maps[i][j] == 'B':
            end = (i, j)
        elif maps[i][j] == 'L':
            start = (i, j)
        elif maps[i][j] == 'R':
            nomap = (i,j)
        
        if start and end and nomap:
            break

q = deque()
q.append(start)
a,b = start

while q:
    x, y= q.popleft()

    for i in range(4):

        nx, ny = x+dx[i], y+dy[i]

        if nx < 0 or ny < 0 or nx >= 10 or ny >= 10:
            continue
        if (nx, ny) == nomap:
            continue
        if maps[nx][ny] == '.' and not visited[nx][ny]:
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))
        
        if (x, y) == end:
            break
        
        

score = []
for i in range(4):
    nx, ny = x+dx[i], y+dy[i]
    if nx >= 0 and nx < 10 and ny >= 0 and ny < 10:

        if visited[nx][ny] > 0:
            score.append(visited[nx][ny])

print(min(score)+1)