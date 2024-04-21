a, b= map(int, input().split())

num = [x for x in range(1, b+1) if x%a==0]

answer = 1

for n in num:
    answer*=n

print(answer)