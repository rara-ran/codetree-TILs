import sys

INT_MAX = sys.maxsize
INT_MIN = sys.maxsize

n = int(input())
arr = list(map(int, input().split()))

min_val = INT_MAX

for x in range(1, n+1):
    sum_val=0
    for i in range(n):
        sum_val += arr[i] * abs(i+1-x)
    min_val = min(min_val, sum_val)

print(min_val)