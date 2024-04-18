n = int(input())
number = []
block = 0
answer = 0
for _ in range(n):
    number.append(int(input()))
num = sum(number)//n
number.sort()

while (number.count(num)) != n:
    
    block = (number[-1]-number[0])//2
    number[0] += block
    number[-1] -= block
    number.sort()
    answer += block

print(answer)