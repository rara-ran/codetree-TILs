n = int(input())

arr = [['']*n for _ in range(n)]
num = 65
for i in range(n):
    print('  '*i, end='')
    for j in range(n-i):
        print(chr(num+j), end=' ')
    num += (j+1)
    print()