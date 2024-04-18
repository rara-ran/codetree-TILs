n = int(input())

score = [0, 0, 0]
state = 6
rank = 7 # 0, 1, 2: A, B, C 단독 1등    3,4,5: A,B  B,C  C,A 2명 1등    6: A,B,C 3명 1등
count = 0

def output_state(score,max_arr,max_v):
    if len(max_arr) == 1:
        state = score.index(max_v)

    elif len(max_arr) == 2:
        test_arr = [x for x in range(3) if score[x]==max_v]
        if test_arr == [0,1]:
            state = 3
        elif test_arr == [1,2]:
            state = 4
        else:
            state = 5

    else:
        state = 6
        
    return state
        

for _ in range(n):
    cmd, s = map(str, input().split())
    s = int(s)
    if cmd=='A':
        score[0] += s
    elif cmd=='B':
        score[1] += s
    else:
        score[2] += s

    max_v = max(score)
    max_arr = [x for x in score if x == max_v]
    post_state = output_state(score, max_arr, max_v)
    if post_state != state:
        count += 1
    state = post_state


print(count)