n, t = map(int, input().split())

if t == 1:
    for i in range(1, n+1):
        print('*'*i)

elif t == 2:
    for i in range(n, 0, -1):
        print('*'*i)

elif t == 3:
    for i in range(1, n+1):
        print(' '*(n-i), end='')
        print('*'*(2*i-1))