# 걍 점화식이랑 비슷

n = int(input())
memo = [-1]*(n+1)

def square(n):
    if memo[n] != -1:
        return memo[n]

    if n == 1 or n == 2:
        return n
    else:
        memo[n] = square(n-1) + square(n-2)
    
    return memo[n]

print(square(n)%10007)