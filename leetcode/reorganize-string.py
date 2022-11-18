import collectiocns
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        d = collections.defaultdict(int)
        for c in s: d[c] += 1
        arr = list(
            zip(
                list(
                    map(lambda n: n*-1, d.values())
                ), d.keys()
            )
        )
        heapq.heapify(arr)
        
        rearranged, broken = [], False
        while arr:
            freq, letter = heapq.heappop(arr)
            freq += 1
    
            if freq < 0:
                heapq.heappush(arr, (freq, letter))
                
            if rearranged and (rearranged[-1] == letter): 
                broken = True
                break
            
            rearranged.append(letter)
                
        return rearranged if not broken else ""
            
        
    
collections.defaultdict(int)
# 3:23
s = Solution()
print(s.reorganizeString("aab"))
