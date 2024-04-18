n = int(input())
number = list(map(int, input().split()))

# min 값 구하고 리스트에서 빼자 + 처음 min 값은 여러 개 있어도 무방

# 그 뒤에 min 값 구하면 걍 두번 째 작은 수
def solution(n, number):
    mini = min(number)
    answer = 0

    num_arr = [x for x in number if x != mini]
    if not num_arr:     return -1
    
    min_v = min(num_arr)

    state = [x for x in num_arr if x == min_v]
    if len(state) >= 2: # 두번째로 작은 수 여러개
        answer = -1
    else: # 두번째로 작은 수 없는 경우도 구현
        answer = number.index(min_v) + 1

    return answer

print(solution(n, number))