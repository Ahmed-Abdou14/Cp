_, stones = input(), list(map(int, input().split(' ')))
stones_sorted = sorted(stones)
for i in range(1, len(stones_sorted)):
    stones_sorted[i] += stones_sorted[i-1]
    stones[i] += stones[i-1]
for i in range(int(input())):
    t, l, r = list(map(lambda x: int(x)-1, input().split(' ')))
    print(
        stones[r] - (stones[l-1] if l-1 >= 0 else 0)
        if t == 0 else 
        stones_sorted[r] - (stones_sorted[l-1] if l-1 >= 0 else 0)
    )
