from typing import List
from numpy import sort

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        weights = [0]*10001
        for n in nums:
            weights[n]+=n
        def rob(nums: List[int]) -> int:
            for i in range(1, len(nums)):
                nums[i] = max(nums[i] + (nums[i-2] if i >= 2 else 0), nums[i-1])
            return nums[-1]
        return rob(weights)
    
sol = Solution()
print(sol.deleteAndEarn([3,4,2]))
print(sol.deleteAndEarn([2,2,3,3,3,4]))