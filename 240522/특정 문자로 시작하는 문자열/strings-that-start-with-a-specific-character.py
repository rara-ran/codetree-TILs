n = int(input())
chr_li = []
for _ in range(n):
    chr_li.append(input())
alpha = input()
chr_arr = [x for x in chr_li if x[0] == alpha]
cnt = len(chr_arr)

answer = sum([len(x) for x in chr_arr])/cnt

print(cnt, f"{answer:.2f}")