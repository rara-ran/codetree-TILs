n = int(input())
dp = [0]*(n+1)
max_v = 0

T, P = [], []

for _ in range(n):
    t, p = map(int, input().split())
    T.append(t); P.append(p)

for i in range(n):
    if T[i]+i > n:
        continue
    max_v = max(dp[i], max_v)
    dp[i+T[i]] = max(dp[i+T[i]], max_v + P[i])

print(max(dp))