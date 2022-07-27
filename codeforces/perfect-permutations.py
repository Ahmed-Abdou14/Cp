tests = int(input())
while tests > 0:
    tests -= 1
    n = int(input())
    ans = list(range(1,n+1))
    for i in range(len(ans)-1, 0, -2):
        ans[i], ans[i-1] = ans[i-1], ans[i]
    print(' '.join(map(lambda x: str(x), ans)))