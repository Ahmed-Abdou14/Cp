import sys
import os.path

def li(): return [int(i) for i in input().split()]
def si(): return input()

if (os.path.exists('input.txt')):
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")
    sys.stderr = open("error.txt", "w")
    
_, ms= si(), sorted(li())
i,j, = 0, len(ms)-1
while(ms[i]*2 < ms[j]):
    l, r = ms[j] / ms[i+1], ms[j-1] / ms[i]
    if l == r: 
        i+=1
        if ms[j]/2 > ms[i]:
            i+=1
    if l > r: j-=1
    else: i+=1
