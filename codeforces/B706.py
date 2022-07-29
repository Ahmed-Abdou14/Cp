from bisect import bisect_right
_, prices = input(), sorted(list(map(int, input().split(' '))))
for i in range(int(input())): print(bisect_right(prices, int(input())))
