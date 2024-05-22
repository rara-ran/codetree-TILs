a1, a2 = map(int, input().split())
num = [a1, a2]
for _ in range(8):
    an = a2 + 2*a1
    num.append(an)
    a2, a1 = an, a2

print(*num)