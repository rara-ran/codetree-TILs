n = int(input())

num = [x for x in range(9, 0, -1)]

answer = []
s = ''

for i in range(n**2+1):
    if len(s) == 4:
        answer.append(s)
        s = ''
    s += str(num[i%9])    

for a in answer:
    print(a)