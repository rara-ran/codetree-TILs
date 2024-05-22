n = int(input())

arr = [['']*n for _ in range(n)]
num = 64
for i in range(n):
    print('  '*i, end='')
    for j in range(n-i):
        num += 1
        if num > 90:
            num = 65
        print(chr(num), end=' ')
    print()