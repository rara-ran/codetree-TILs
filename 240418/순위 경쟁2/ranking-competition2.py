n = int(input())


score_board = [0, 0]
state = 2
count = 0


for _ in range(n):
    cmd, s = map(str, input().split())
    s = int(s)

    if cmd == 'A':
        score_board[0] += s
    else:
        score_board[1] += s
    
    max_v = max(score_board)

    mini = [x for x in score_board if x == max_v] # 2개 이상 대비해서
    idx = score_board.index(max_v) # 1개일 때
    
    if len(mini) == 2: # A, B 점수 동점 됐을 경우
        if state != 2:
            count += 1
            state = 2
    else:
        if state != idx:
            count += 1
            state = idx

print(count)