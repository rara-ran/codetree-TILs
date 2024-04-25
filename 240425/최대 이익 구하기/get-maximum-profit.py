n = int(input())
dp = [0]*(n+1)

T, P = [], []

for _ in range(n):
    t, p = map(int, input().split())
    T.append(t); P.append(p)

maxV = 0
for i in range(n):
    maxV = max(dp[i], maxV)
    if i + T[i] > n:
        continue
    dp[i+T[i]] = max(dp[i+T[i]], maxV + P[i])

print(max(dp))