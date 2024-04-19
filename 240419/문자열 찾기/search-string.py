s = input()

score = [0,0]

for i in range(len(s)-2):
    state = s[i:i+3]

    if 'KOI'== state:
        score[0]+=1
    elif 'IOI' == state:
        score[1]+=1

print(*score)