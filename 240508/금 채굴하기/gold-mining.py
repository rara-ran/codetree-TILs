def make_gold(k, maps, n):
    # gold_cnt = 0
    arr = []
    dx, dy = [k,-k,0,0], [0,0,k,-k] # 상하좌우

    if k == 1:
        for i in range(n):
            for j in range(n):
                gold_cnt = 0
                if maps[i][j] == 1:
                    gold_cnt += 1
                for d in range(4):
                    if i+dx[d] < 0 or j+dy[d] < 0 or i+dx[d] >= n or j+dy[d] >= n:
                        continue
                    if maps[i+dx[d]][j+dy[d]] == 1:
                        gold_cnt += 1
                arr.append(gold_cnt)
        return arr

    else:
        for i in range(n):
            for j in range(n):

                gold_cnt = 0
                
                for idx in range(k):
                    for idy in range(j-idx, j+idx+1):
                        if i-k+idx < 0 or i-k+idx >= n or idy >= n or idy < 0:
                            continue
                        if maps[i-k+idx][idy] == 1:
                            gold_cnt += 1
                        if i+k-idx < 0 or i+k-idx >= n:
                            continue
                        if maps[i+k-idx][idy] == 1:
                            gold_cnt += 1
                for c in range(j-k, j+k+1):
                    if c < 0 or c >= n:
                        continue
                    if maps[i][c] == 1:
                        gold_cnt += 1
                
                arr.append(gold_cnt)
        return arr



n, m = map(int,input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            cnt += 1

cost = m*cnt
answer = []
if cnt >= 1:
    answer.append(1)

for k in range(1, n):
    if k**2 + (k+1)**2 > cost:
        break

    gold_set = set(make_gold(k, maps, n))
    if gold_set:
        ans_arr = [x for x in gold_set if k**2 + (k+1)**2 <= x*m]
    if ans_arr:
        answer.append(max(ans_arr))

if answer:
    print(max(answer))
else:
    print(0)