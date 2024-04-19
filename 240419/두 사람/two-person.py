value = 0
for _ in range(2):
    is_age, is_male = 0, 0
    age, sex = map(str, input().split())
    if int(age) >= 19:
        is_age = 1
    if sex == 'M':
        is_male = 1
    
    if is_age and is_male:
        value = 1
    
print(value)