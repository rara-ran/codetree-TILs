a, b = map(int, input().split())

for idx in range(2, 9, 2):
    for num in range(b, a-1, -1):
        print(num, '*', idx, '=', num*idx, end=' ')
        if num != a:
            print('/', end=' ')
    print()