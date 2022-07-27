from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i] + (nums[i-2] if i >= 2 else 0), nums[i-1])
        return nums[-1]
    
sol = Solution()    
print(sol.rob([1, 2, 3, 1])) #4
print(sol.rob([2,7,9,3,1])) #12
print(sol.rob([2, 1, 1, 2])) #4
