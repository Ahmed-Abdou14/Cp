ans, _, l = 0, input(), list(map(int, input().split(' ')))
p, count = None, 0
for n in l:
    if n != p:
        ans += count*(count-1)//2
        p = n
        count = 1
    else: count += 1
print(len(l) + ans + count*(count-1)//2)
