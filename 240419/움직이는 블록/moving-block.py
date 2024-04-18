n = int(input())
number = []
block = 0
answer = 0
for _ in range(n):
    number.append(int(input()))
num = sum(number)//n
number.sort()

while (number.count(num)) != n:

    want_block = num - number[0]
    if number[-1] - want_block >= num:
        number[-1] -= want_block
        number[0] += want_block
        answer += want_block
    else:
        able_block = number[-1] - num
        number[0] += able_block
        number[-1] -= able_block
        answer += able_block

    number.sort()
 

print(answer)