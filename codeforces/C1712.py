for _ in range(int(input())):
    __ = int(input())
    arr = list(map(int, input().split(' ')))
    si = __-1
    for i in range(len(arr)-2,-1,-1):
        if arr[i] == arr[i+1]: si = i
        else: break
    
    print(len(set(arr[:-1])))