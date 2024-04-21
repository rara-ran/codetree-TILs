a, b= map(int, input().split())

num = [x for x in range(a, b+1) if x%6==0]
number = [x for x in num if not x%8==0]

print(sum(number))