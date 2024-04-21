a = int(input())

num = [x for x in range(1, a+1) if not (x%2==0 and x%4!=0)]

num_1 = [x for x in num if (x//8) %2 == 1] 

num_2 = [x for x in num_1 if not x%7 < 4 ]

print(*num_2)