from collections import defaultdict
from bisect import insort_right
from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        maxx = -1
        sums_to_nums = defaultdict(list)
        for num in nums:
            sum_of_digits = self.get_sum_of_digits(num)
            grouped_nums = sums_to_nums[sum_of_digits]
            if len(grouped_nums) >= 2:
                grouped_nums[0] = max(grouped_nums[0], num)
            else:
                insort_right(grouped_nums, num)
            maxx = max(maxx, sum(grouped_nums[-2:]))
        # print(sums_to_nums)
        return maxx
        
        
    def get_sum_of_digits(self, num: int) -> int:
        sum = 0
        while num > 0:
            sum += num % 10
            num = num // 10
        return sum
    
sol = Solution()
print(sol.maximumSum([18,43,36,13,7]))