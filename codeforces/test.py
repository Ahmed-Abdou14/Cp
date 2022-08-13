_, arr  = input(), list(input())
for i in range(len(arr)):
    arr[i] = 1 if arr[i] == '"' else 0 if arr[i] == '.' else -1
def bfs(arr, i):
    if i >= len(arr): return 0
    elif arr[i] < 0: return -1111
    else: 
        return arr[i] + max([
            bfs(arr, i+1), 
            bfs(arr, i+3), 
            bfs(arr, i+5)])
print(max(bfs(arr, 0), -1))


# import sys
# from os import path
# sys.stdin = open('lepus.in', 'r')
# sys.stdout = open('lepus.out', 'w')
# _, arr = sys.stdin.readline().strip(), list(sys.stdin.readline().strip())
# for i in range(len(arr)):
#     arr[i] = 1 if arr[i] == '"' else 0 if arr[i] == '.' else -1


# def bfs(arr, i):
#     if i >= len(arr):
#         return 0
#     elif arr[i] < 0:
#         return -1111
#     else:
#         return arr[i] + max([bfs(arr, i+1), bfs(arr, i+3), bfs(arr, i+5)])

# sys.stdout.write(str(max(bfs(arr, 0), -1)))



import sys
from os import path
sys.stdin = open('lepus.in', 'r')
sys.stdout = open('lepus.out', 'w')
_, arr = sys.stdin.readline().strip(), list(sys.stdin.readline().strip())
for i in range(len(arr)):
    arr[i] = 1 if arr[i] == '"' else 0 if arr[i] == '.' else -1

for i in range(1, len(arr)):
    add = max([
        max(-1, arr[i-1]),
        max(-1, arr[i-3] if i > 2 else -1),
        max(-1, arr[i-5] if i > 4 else -1)
    ])
    arr[i] += add
jumps = arr[-1]
sys.stdout.write(str(max(jumps, -1)))
