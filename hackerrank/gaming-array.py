import os

def gamingArray(arr):
    plays, max = 0, 0
    for i in range(0, len(arr)-1):
        if arr[i] >  max:
            playes+=1
            max = arr[i]
            
    return 'BOB' if plays%2==0 else 'ANDY'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = gamingArray(arr)

        fptr.write(result + '\n')

    fptr.close()
