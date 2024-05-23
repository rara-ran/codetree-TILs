n, m = map(int, input().split())
graph = {key:[] for key in range(1, n+1)}
visited = [0]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(vertex):
    for point in graph[vertex]:
        if not visited[point]:
            visited[point] = 1
            dfs(point)

visited[1] = 1
dfs(1)

print(visited.count(1)-1)