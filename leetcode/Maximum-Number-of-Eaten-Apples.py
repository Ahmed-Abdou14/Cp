from typing import List
import heapq

class Batch:
    
    def __init__(self, count: int, start: int, ttl: int) -> None:
        self.count = count
        self.start = start
        self.end = start + ttl
        
    def __eq__(self, other):
        return self.end == other.end
    
    def __gt__(self, other):
        return self >= other
    
    def __ge__(self, other):
        return self.end >= other.end and self.start >= other.start
    
    def __lt__(self, other):
        return self <= other

    def __le__(self, other):
        return self.end <= other.end and self.start <= other.start
    
    def __repr__(self) -> str:
        return self.__dict__.__repr__()
        

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        
        q = []
        for i, (count, ttl) in enumerate(zip(apples, days)):
            if count > 0:
                q.append(Batch(count, i, ttl))
        
        heapq.heapify(q)
        
        eaten, day = 0, 0
        while len(q) > 0:
            b: Batch = heapq.heappop(q)
            if b.start > day:
                b.start -= 1
                heapq.heappush(q, b)       
                # day += 1
            elif b.end > day:
                eaten += 1
                if b.count > 1:
                    b.count -= 1
                    heapq.heappush(q, b)    
                day += 1
        
        return eaten
    
    # def recurseive_print(self, q):
    #     if len(q):
    #         x = heapq.heappop(q)
    #         print(x)
    #         self.recurseive_print(q)
    #         heapq.heappush(q, x)
    #     else: print()
        
        
sol = Solution()
print(sol.eatenApples([9, 2], [3, 5]))
print(sol.eatenApples([1, 2, 3, 5, 2], [3, 2, 1, 4, 2]))

        