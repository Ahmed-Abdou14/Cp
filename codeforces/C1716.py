t = int(input())

for _ in range(t):
    size, arr, clock = int(input()), [
        list(map(int, input().split(' '))),
        list(map(int, input().split(' ')))
    ], 0
    visited, ci, cj = 1, 0, 0
    while visited < size:
        n1 = n2 = 10**9+1
        if ci == 0:
            break
        else: #ci == 1
            break