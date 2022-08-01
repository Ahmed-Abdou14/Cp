d = {'A':2, 'B':2,'C':2}

for i in range(3):
    c1, sign, c2 = list(input())
    if sign == '<': d[c1]-=1
    else: d[c2] = d[c2]-1

ans = [-1,-1,-1]
if sum(d.values()) == 3:
    for k, v in d.items():
        ans[v] = k
    print(''.join(ans))
else: print('Impossible') 