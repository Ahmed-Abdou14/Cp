# import math

# def forward_steps(s,t):
#     m = math.ceil(t/s) if t>=s else 0
#     return math.ceil(m/2) + max(s*(m+1)-t, 0)
# def back_n_forth_steps(s,t):
#     if t%2==1: return 10**10
#     m = math.ceil(t/s)
#     return math.ceil(m/2)+s-t//(m if m%2==0 else m+1)

# s, t = list(map(int, input().split(" ")))

# s1 = forward_steps(s, t)
# s2 = back_n_forth_steps(s,t)

# print(s1,s2,min(s1,s2))


s, t = list(map(int, input().split(" ")))
clicks = 0
while t > s:
    clicks+=1
    if t%2==0: t//=2
    else: t+=1
print(clicks+s-t)
        
