from fractions import Fraction


def reducefract(n, d):
    def gcd(n, d):
        while d != 0:
            t = d
            d = n % d
            n = t
        return n
    greatest = gcd(n, d)
    n //= greatest
    d //= greatest
    return f"{n}/{d}"

d, w, b = list(map(int, input().split(' ')))
t = min(w, b)-1
for i  in range(min(w,b), d+1):
   if i%w == i%b == 0: 
       t+=min(w,b)
f = reducefract(t, d)
print(f)
    
