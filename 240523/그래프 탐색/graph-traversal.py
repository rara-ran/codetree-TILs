n, m = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
visited = [0]*(n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def dfs(vertex):
    for curr_v in range(1, n+1):
        if graph[vertex][curr_v] and not visited[curr_v]:
            visited[curr_v] = 1
            dfs(curr_v)

visited[1] = 1
dfs(1)

print(visited.count(1)-1)