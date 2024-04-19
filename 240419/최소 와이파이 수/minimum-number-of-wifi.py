def install_wifi(n, m, number):
    wifi = 0
    people_idx = 0
    if m == 0:
        return number.count(1)
    idx = 0
    while number.count(0) != n:
        if number[idx] == 1:
            people_idx += 1
        idx += 1

        if people_idx == m:
            for i in range(idx-m, idx+m+1):
                number[i] = 0
            people_idx = 0
            wifi += 1
    return wifi

n, m = map(int, input().split())
number = list(map(int, input().split()))
    
print(install_wifi(n, m, number))