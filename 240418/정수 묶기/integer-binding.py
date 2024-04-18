answer = 0

n = int(input())
number = []
for _ in range(n):
    number.append(int(input()))

small_num = [-x for x in number if x < 0]
large_num = [x for x in number if x > 0]
small_num.sort()
large_num.sort()

while small_num:
    if len(small_num) == 1:
        answer += -(small_num.pop())
    else: # 앞에 있는 값끼리
        answer += (small_num.pop()*small_num.pop())

while large_num:
    if len(large_num) == 1:
        answer += large_num.pop()
    else:
        a = large_num.pop()
        b = large_num.pop()

        if a == 1 or b == 1:
            answer+= (a+b)
        else:
            answer += (a*b)

print(answer)