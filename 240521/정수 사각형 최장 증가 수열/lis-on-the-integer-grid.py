from collections import deque
n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]

def bfs(maps,i,j):
    dx, dy = [-1,1,0,0], [0,0,-1,1]
    visited = [[0]*n for _ in range(n)]
    count = 1
    q = deque()
    q.append((i,j))
    visited[i][j] = 1
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            
            if maps[nx][ny] > maps[x][y] and not visited[nx][ny]:
                q.append((nx, ny))
                
                visited[nx][ny] = 1
                x, y = nx, ny
                count += 1
                break
    
    return count


answer = []

for i in range(n):
    for j in range(n):
        answer.append(bfs(maps,i,j))

print(max(answer))