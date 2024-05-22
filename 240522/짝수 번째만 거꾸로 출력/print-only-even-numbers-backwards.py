s = input()

arr = [s[i] for i in range(len(s)) if i%2==1]
arr.reverse()

for a in arr:
    print(a, end='')