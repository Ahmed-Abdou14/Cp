class Solution(object):
    def prefixesDivBy5(self, nums):
        for i in range(1, len(nums)): nums[i] += nums[i-1]*2
        return list(map(lambda n: n % 5 == 0, nums))
    
sol = Solution()
print(sol.prefixesDivBy5([0, 1, 1]))
print(sol.prefixesDivBy5([1, 1, 1]))