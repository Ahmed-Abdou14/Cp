for _ in range(int(input())):
    n, k = list(map(int, input().split(' ')))
    arr = list(map(int, input().split(' ')))
    print(len(list(filter(lambda x: x > k, arr[:k]))))