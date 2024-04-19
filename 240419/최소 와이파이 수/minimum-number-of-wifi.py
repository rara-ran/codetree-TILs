def install_wifi(n, m, number):
    
    if m == 0: # 0위치 이내
        return number.count(1)

    if number.count(0) == n: # 아무도 안 살면
        return 0

    wifi = 0
    people_idx = []
    idx = 0

    while idx < n:
        if number[idx] == 1:
            people_idx.append(idx)
        idx += 1
        if people_idx:
            if idx - people_idx[0] == m :
                if idx+m < n and idx-m >=0:
                    for i in range(idx-m, idx+m+1): # 
                        number[i] = 0
                else: 
                    if idx+m >= n:
                        for i in range(idx-m, n):
                            number[i] = 0
                    elif idx-m < 0:
                        for i in range(idx+m+1):
                            number[i] = 0
                people_idx = []
                wifi += 1

        # print(number)
    return wifi

n, m = map(int, input().split())
number = list(map(int, input().split()))
    
print(install_wifi(n, m, number))