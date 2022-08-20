for _ in range(int(input())):
    n = int(input())
    arr = [i+2 if i % 2 == 0 else i for i in range(n)]
    print(' '.join(map(str, arr)))
    