n = int(input())

for i in range(1, n+1):
    print(' '*(n - i), end='')
    for j in range(1, i+1):
        print('*', end=' ')
    print(' '*(n - i))

for i in range(n-1, 0, -1):
    print(' '*(n - i), end='')
    for j in range(1, i+1):
        print('*', end=' ')
    print(' '*(n - i))