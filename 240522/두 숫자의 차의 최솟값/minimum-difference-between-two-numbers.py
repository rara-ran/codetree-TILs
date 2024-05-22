n = int(input())
num = list(map(int, input().split()))
answer = []
for i in range(1, n):
    answer.append(num[i]-num[i-1])

print(min(answer))