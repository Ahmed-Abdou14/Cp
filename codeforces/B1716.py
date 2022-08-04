n = int(input())
while n > 0:
    n-=1
    s = int(input())
    arr = [str(i) for i in range(1, s+1)]
    print(s)
    print(' '.join(arr))
    for i in range(s-1, 0,-1):
        arr[i], arr[i-1] = arr[i-1], arr[i]
        print(' '.join(arr))