n = int(input())

number = [x for x in range(2, n+1)]
answer = 0

for num in number:
    n//=num
    if n <= 1:
        answer = num
        break

print(answer)