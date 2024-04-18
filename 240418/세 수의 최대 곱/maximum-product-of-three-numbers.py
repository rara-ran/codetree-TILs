n = int(input())
number = list(map(int, input().split()))

number.sort()

a,b,c = number[-1], number[-2], number[-3]
cost_1 = a*b*c
x,y,z = number[0], number[1], number[-1]
cost_2 = x*y*z

print(max(cost_1, cost_2))