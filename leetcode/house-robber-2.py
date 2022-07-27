from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        elif len(nums) == 2 or len(nums) == 3: return max(nums)
        
        def rob_original(nums: List[int]) -> int:
            nums[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                nums[i] = max(nums[i] + nums[i-2], nums[i-1])
            return nums[-1]
    
        return max(rob_original(nums[:-1]), rob_original(nums[1:]))
    
sol = Solution()
print(sol.rob([2, 3, 2]))
print(sol.rob([1, 2, 3, 1]))
print(sol.rob([1,2,3]))