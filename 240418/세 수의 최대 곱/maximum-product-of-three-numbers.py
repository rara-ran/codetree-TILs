n = int(input())
number = list(map(int, input().split()))
plus_number = [x for x in number if x > 0]
minus_number = [-x for x in number if x < 0]

plus_number.sort()
minus_number.sort()
m = plus_number.pop()

plus_value = m*(plus_number.pop())*(plus_number.pop())
minus_value = m*minus_number.pop()*minus_number.pop()

print(max(plus_value, minus_value))