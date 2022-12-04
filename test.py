from functools import wraps
import math
import time

def timeit(func):
    @wraps(func)
    async def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = await func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'def {func.__name__}{args} --> {total_time:.4f}s', flush=True)
        return result
    return timeit_wrapper

def mask1(s1: str, s2: str, mask: chr) -> str:
    arr = list(s2)
    for i, c1 in enumerate(s1):
        if c1 == mask:
            arr[i] = c1
    return "".join(arr)

def mask2(s1: str, s2: str, mask: chr) -> str:
    return "".join([c2 if c1 != mask else c1 for c1, c2 in zip(s1, s2)])


def mask3(s1: str, s2: str, mask: chr) -> str:
    s3 = ""
    for c1, c2 in zip(s1, s2):
        if c1 == mask:
            s3 += c1
        else:
            s3 += c2
            
    return s3

import random

loop = 100

time_for_mask1 = 0
time_for_mask2 = 0
time_for_mask3 = 0

for i in range(loop):

    print(i)
    
    size = random.randint(10000, 1000000)
    s1 = "".join([chr(random.randint(97, 122)) for i in range(size)])
    s2 = "".join([chr(random.randint(97, 122)) for i in range(size)])
    mask = chr(random.randint(97, 122))
    
    start_time = time.perf_counter()
    mask1(s1, s2, mask)
    end_time = time.perf_counter()
    time_for_mask1 += end_time-start_time

    start_time = time.perf_counter()
    mask2(s1, s2, mask)
    end_time = time.perf_counter()
    time_for_mask2 += end_time-start_time

    start_time = time.perf_counter()
    mask3(s1, s2, mask)
    end_time = time.perf_counter()
    time_for_mask3 += end_time-start_time
    
    
avg_time_mask1 = time_for_mask1/loop
avg_time_mask2 = time_for_mask2/loop
avg_time_mask3 = time_for_mask3/loop

def percent(n1, n2):
    maxx = max(n1, n2)
    minn = min(n1, n2)
    return maxx*100/minn
    diff = maxx-minn
    

print(f"""
    time for task 1: {avg_time_mask1}
    time for task 2: {avg_time_mask2}
    time for task 3: {avg_time_mask3}
""")
