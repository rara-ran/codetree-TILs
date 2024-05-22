a, b = map(int, input().split())
num = []
answer = 0
while a > 1:
    num.append(a%b)
    a//=b

for i in range(b):
    answer += num.count(i)**2

print(answer)