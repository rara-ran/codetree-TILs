n = int(input())

maps = [list(map(int, input().split())) for _ in range(n)]

def find_coin(row, col, maps):
    answer = 0
    for r in range(row, row+3): # row부터 시작
        for c in range(col, col+3):
            answer += maps[r][c]
    
    return answer

coin = []

for i in range(n-2):
    for j in range(n-2):
        coin.append(find_coin(i, j, maps))
        
print(max(coin))