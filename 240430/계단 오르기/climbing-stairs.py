n = int(input())
memo = [-1]*(n+1)

def stair(n):
    if memo[n] != -1:
        return memo[n]
    if n == 2 or n == 3:
        return 1
    elif n == 1:
        return 0
    else:
        memo[n] = stair(n-2) + stair(n-3)
    
    return memo[n]

    
print(stair(n)%10007)