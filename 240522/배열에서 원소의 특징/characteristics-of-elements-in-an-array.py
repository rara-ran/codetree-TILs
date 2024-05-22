num = list(map(int, input().split()))

for n in num:
    if n%3==0:
        idx = num.index(n)
        break

print(num[idx-1])