n = int(input())
num = list(map(int, input().split()))

idx = 0
i=0

for nnn in num:
    i += 1
    if nnn == 2:
        idx += 1
        
    if idx == 3:
        print(i)
        break