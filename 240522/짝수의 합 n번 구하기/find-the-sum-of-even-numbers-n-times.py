n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    num = [x for x in range(a, b+1) if x%2==0]
    print(sum(num))