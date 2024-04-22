cnt = 0
n = int(input())
while n < 1000:
    if n %2 == 1:
        n*=2
        n +=2
    else:
        n *=3
        n+=1

    cnt += 1

print(cnt)