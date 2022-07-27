from ast import List
from operator import index, le

class Solution:
    def canBeIncreasing(self, nums):
        removed = 0
        for i in range(len(nums)):
            if i < len(nums)-1 and nums[i] < nums[i+1]:
                if i < len(nums)-2 and nums[i] < nums[i+2]:
                    removed+=1
                    if removed > 1: return False
            if i > 0 and i < len(nums)-1 and nums[i-1] < nums[i+1]:
                removed += 1
                if removed > 1: return False
        return True                 

    def canBeIncreasing2(self, nums):
        indexes = []
        for i in range(len(nums)-1):
            if(nums[i] >= nums[i+1]):
                indexes.append(i)

        if len(indexes) > 1:
            return False
        if len(indexes) == 0:
            return True
        i = indexes[0]
        if i > 0 and i < len(nums)-1 and nums[i-1] < nums[i+1]:
            return True
        if i > 0 and i < len(nums)-2 and nums[i] < nums[i+2]:
            return True
        return False

      
sol = Solution()
print(sol.canBeIncreasing2([105,924,32,968]))