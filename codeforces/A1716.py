n = int(input())
while n > 0:
    n -= 1
    t = int(input())
    m = t//3
    m += 1 if t%3 > 0 else 0
    print(m if t != 1 else 2)