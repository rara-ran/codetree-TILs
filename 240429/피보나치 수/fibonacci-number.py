n = int(input())
memo = [-1]*(n+1)

def fibo(n):

    if memo[n] != -1:
        return memo[n]
    if n <= 2:
        return 1
    else:
        memo[n] = fibo(n-1) + fibo(n-2)
    
    return memo[n]
        
    
print(fibo(n))