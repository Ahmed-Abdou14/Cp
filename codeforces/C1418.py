for i in range(int(input())):
    _, l = input(), list(map(int, input().split(' ')))
    for i in range(1, len(l)): l[i] += min(l[max(0, i-3):i])
    print(min(l[-3:]))