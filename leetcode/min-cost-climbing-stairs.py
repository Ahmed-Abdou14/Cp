
from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2, len(cost)):
            cost[i] += min(cost[i-2], cost[i-1])
        return min(cost[-2:])
    
sol = Solution()
print(sol.minCostClimbingStairs([10,15,20]))
print(sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))