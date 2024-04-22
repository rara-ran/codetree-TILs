n = int(input())

for i in range(n-1):
    print('* '*(n - i))
    print('* '*(i+1))

print('* '*1)
print('* '*n)