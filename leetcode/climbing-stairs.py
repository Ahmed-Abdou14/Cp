class Solution:
    def climbStairs(self, n: int) -> int:
        n1 = 1
        n2 = 1
        while n != 1:
            tmp = n2
            n2 += n1
            n1 = tmp
            n -= 1
        return n2
    
sol = Solution()
print(sol.climbStairs(1))
print(sol.climbStairs(2))
print(sol.climbStairs(3))
print(sol.climbStairs(4))
print(sol.climbStairs(5))

"""
fibbonacci
1 2 3 5 8 13 21
"""