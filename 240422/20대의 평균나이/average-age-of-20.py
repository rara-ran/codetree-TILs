age = []
num = (int(input()))

while num < 30 and num > 19 :
    age.append(num)
    num = int(input())

answer=sum(age)/len(age)
print(format(answer, ".2f"))