a, b= map(int, input().split())
answer = ''

if a <= 0:
    answer = 0
else:
    for i in range(b):
        answer += str(a)

print(answer)