n = int(input())

number = [int(input()) for _ in range(n)]

answer = [x for x in number if x%3==0 and x%2==1]
answer.sort()

for a in answer:
    print(a)