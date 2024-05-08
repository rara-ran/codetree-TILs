def make_gold(k, maps, n):
    # gold_cnt = 0
    arr = []
    dx, dy = [k,-k,0,0], [0,0,k,-k] # 상하좌우

    if k == 0:
        return [1]

    elif k == 1:
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
                
                for d in range(4):
                    
                    if i+dx[d] < 0 or j+dy[d] < 0 or i+dx[d] >= n or j+dy[d] >= n:
                        continue
                    if maps[i+dx[d]][j+dy[d]] == 1:
                        gold_cnt += 1
                    

                for r in range(i-(k-1), i+(k-1)+1):
                    for c in range(j-(k-1), j+(k-1)+1):
                        
                        if r < 0 or c < 0 or r >= n or c >= n:
                            continue
                        if maps[r][c] == 1:
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

for k in range(n):
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