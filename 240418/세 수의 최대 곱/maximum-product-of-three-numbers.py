n = int(input())
number = list(map(int, input().split()))

def make_maxV(n, number):
    if n == 3:
        return number.pop()*number.pop()*number.pop()

    plus_number = [x for x in number if x > 0]
    minus_number = [-x for x in number if x < 0]

    plus_number.sort()
    minus_number.sort()

    if len(plus_number) >= 3 and len(minus_number) >= 2:
        m = plus_number.pop()

        plus_value = m*plus_number.pop()*plus_number.pop()
        minus_value = m*minus_number.pop()*minus_number.pop()
        return (max(plus_value, minus_value))

    elif len(plus_number) >= 3 and len(minus_number) < 2:
        return plus_number.pop()*plus_number.pop()*plus_number.pop()
    
    elif len(plus_number) <= 1:
        if len(plus_number) == 1:
            return plus_number.pop()*minus_number.pop()*minus_number.pop()
        else:
            return -minus_number.pop(0)*minus_number.pop(0)*minus_number.pop(0)


print(make_maxV(n, number))