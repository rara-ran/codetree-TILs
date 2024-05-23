def is_range(x, y):
    return 0<=x and x<n and 0<=y and y<m

def can_go(x, y, K):
    if not is_range(x,y):
        return False
    
    if visited[x][y] or maps[x][y] <= K: # 방문했거나 K 이하일 때
        return False
    
    return True

def dfs(x, y, K):
    
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]

        if can_go(nx, ny, K):
            visited[nx][ny] = 1 # 방문처리
            dfs(nx, ny, K)

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

max_arr = []
for mmm in maps:
    max_arr.append(max(mmm))
            
K_max = max(max_arr)
answer = [0]*(K_max+1)

for k_val in range(1, K_max+1):
    sector_cnt = 0
    visited = [[0]*m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] > k_val and not visited[i][j]:
                visited[i][j] = 1 # 방문 처리
                dfs(i, j, k_val)
                sector_cnt += 1
    
    answer[k_val] = sector_cnt
    

max_v = max(answer)
print(max_v, answer.index(max_v))