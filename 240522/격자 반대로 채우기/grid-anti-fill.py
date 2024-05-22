# 홀수일 때
def odd_num(n, maps):
    num = n**2
    for j in range(n):
        if j % 2 == 0:
            for i in range(n):
                maps[i][j] = num
                num -= 1
        else:
            for x in range(n-1, -1, -1):
                maps[x][j] = num
                num -= 1
    return maps

# 짝수일 때
def even_num(n, maps):
    num = n**2
    for j in range(n):
        if j % 2 == 1:
            for i in range(n):
                maps[i][j] = num
                num -= 1
        else:
            for x in range(n-1, -1, -1):
                maps[x][j] = num
                num -= 1
    return maps

n = int(input())

maps = [[0]*n for _ in range(n)]

if n%2==0:
    answer = even_num(n,maps)
else:
    answer = odd_num(n, maps)

for m in answer:
    print(*m)