n = int(input())
num = list(map(int, input().split()))

answer = [x for x in num if x%2==0]
answer.reverse()

print(*answer)