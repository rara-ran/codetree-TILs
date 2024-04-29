n = int(input())

def stair(n):
    if n == 2 or n == 3:
        return 1
    if n == 1:
        return 0
    else:
        return stair(n-2) + stair(n-3)

    
print(stair(n)%10007)