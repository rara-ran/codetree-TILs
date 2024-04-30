# 연속으로 m개 동일한 숫자 몇 개 나오는지 확인하는 함수
def count_num(arr, n, k):
    cnt_arr = []
    cnt = 1
    for i in range(n-1):
        if arr[i] == arr[i+1]:
            cnt+=1
        else:
            cnt_arr.append(cnt)
            cnt = 1
    if cnt:
        cnt_arr.append(cnt)
    
    ans_arr = [1 for x in cnt_arr if x >= k]

    if ans_arr:
        return 1
    else:
        return 0


# 같은 행, 같은 열로 수열 되는지 확인 (2n번 돌리기)
n, k = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
answer = 0
row_check = [[0] for _ in range(n)]

for col in range(n):
    for idx in range(n):
        row_check[idx].append(maps[col][idx])
    answer += (count_num(maps[col], n, k))

for row in range(n):
    answer += (count_num(row_check[row],n,k))

print(answer)