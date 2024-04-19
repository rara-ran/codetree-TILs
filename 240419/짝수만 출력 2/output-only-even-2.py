a, b= map(int, input().split())

if a % 2 == 1:
    a += 1 

for i in range(a, b-1, -1):
    if i % 2 == 0:
        print(i, end=' ')