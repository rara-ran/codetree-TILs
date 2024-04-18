from collections import deque

dx, dy = [0,1], [1,0] # 아래, 오른쪽으로만 이동

n, m, a, b = map(int, input().split())

maps = [[0]*(m+1) for _ in range(n+1)]
visited = [[0]*(m+1) for _ in range(n+1)]

for _ in range(a):
    r, c = map(int, input().split())

    maps[r][c] = 1

for _ in range(b):
    r, c = map(int, input().split())

    maps[r][c] = 2

# 장애물 continue

# 아이템 만나면 count + 1

score = 0

q = deque()
q.append((1,1))

while q:
    x, y = q.popleft()

    for i in range(2):
        nx, ny = x+dx[i], y+dy[i]

        if nx < 1 or ny < 1 or nx > n or ny > m or maps[nx][ny] == 2:
            continue

        if maps[nx][ny] == 0 and not visited[nx][ny]:
            q.append((nx, ny))
            visited[nx][ny] = 1

        elif maps[nx][ny] == 1 and not visited[nx][ny]:
            score += 1
            q.append((nx, ny))
            visited[nx][ny] = 1
        
    
print(score)