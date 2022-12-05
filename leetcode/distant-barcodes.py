from collections import defaultdict
import heapq
from typing import List


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        freqs = defaultdict(int)
        for barcode in barcodes:
            freqs[barcode] += 1
        heap = []
        for barcode, freq in freqs.items():
            heapq.heappush(heap, (-freq, barcode))
        result = []
        prev = None
        while len(heap) > 0:
            freq, barcode = heapq.heappop(heap)
            if prev and prev[0] < 0:
                heapq.heappush(heap, prev)
            result.append(barcode)
            prev = freq + 1, barcode
        return result
    
sol = Solution()
print(sol.rearrangeBarcodes([1,1,1,2,2,2]))
    
        
        
""" 
from typing import List
from collections import Counter, defaultdict
import heapq

class Node:
    def __init__(self, val, count):
        self.val = val
        self.count = count
        
    def __lt__(self, other):
        return self.count >= other.count
    
    def __eq__(self, other):
        return self.count == other.count
    
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        
        freqs = Counter(barcodes)
        
        nodes: List[Node] = []
        for key, val in freqs.items():
            heapq.heappush(nodes,Node(key, val))
            
        builder = []
        prev = None
        while len(nodes) > 0:
            node = heapq.heappop(nodes)
            if prev and prev.count > 0:
                heapq.heappush(nodes, prev)
            builder.append(node.val)
            node.count -= 1
            prev = node
        
        return builder
"""