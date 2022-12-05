from typing import List
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        dp = [[None for _ in range(len(grid[0]))] for _ in range(len(grid))] # (min, max)
        
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                
                if i == j == 0:
                    lowest = highest = grid[i][j]
                elif i == 0:
                    lowest = min(grid[i][j] * dp[i][j-1][0], grid[i][j] * dp[i][j-1][1])
                    highest = max(grid[i][j] * dp[i][j-1][0], grid[i][j] * dp[i][j-1][1])
                elif j == 0:
                    lowest = min(grid[i][j] * dp[i-1][j][0], grid[i][j] * dp[i-1][j][1])
                    highest = max(grid[i][j] * dp[i-1][j][0], grid[i][j] * dp[i-1][j][1])
                else:
                    lowest = min(
                        grid[i][j] * dp[i-1][j][0], grid[i][j] * dp[i-1][j][1],
                        grid[i][j] * dp[i][j-1][0], grid[i][j] * dp[i][j-1][1]
                    )
                    highest = max(
                        grid[i][j] * dp[i-1][j][0], grid[i][j] * dp[i-1][j][1],
                        grid[i][j] * dp[i][j-1][0], grid[i][j] * dp[i][j-1][1]
                    )
                    
                dp[i][j] = (lowest, highest)
                
        return dp[-1][-1][1] % (10**9 + 7) if dp[-1][-1][1] >= 0 else -1
    
sol = Solution()
print(sol.maxProductPath([[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]))