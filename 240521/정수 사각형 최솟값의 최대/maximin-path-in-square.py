n = int(input())

maps = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
route = []

dp[0][0] = maps[0][0]

for i in range(1, n):
    dp[0][i] = min(dp[0][i-1], maps[0][i])
    dp[i][0] = min(dp[i-1][0], maps[i][0])


for i in range(1,n):
    for j in range(1,n):
        dp[i][j] = min(max(dp[i-1][j], dp[i][j-1]), maps[i][j])
    
print(dp[n-1][n-1])