from re import L, S
from flask import g


class Solution:
    def __init__(self):
        self.sizes = dict()
        
    def maxAreaOfIsland(self, grid) -> int:
        self.bfs(grid, 0, 0)
        return max(self.sizes.values()) if len(self.sizes) else 0
    
    def bfs(self, grid, i, j, key=None):
        
        if grid[i][j] >= 1:
            
            if key in self.sizes: self.sizes[key] += 1
            else:
                key = "{}{}".format(i, j)
                self.sizes[key] = 1

            if i < len(grid) - 1: self.bfs(grid, i+1, j, key)
            if j < len(grid[i]) - 1: self.bfs(grid, i, j+1, key)

        elif grid[i][j] == 0:
            
            grid[i][j] = -1
            
            if i < len(grid) - 1: self.bfs(grid, i+1, j)
            if j < len(grid[i]) - 1: self.bfs(grid, i, j+1)

sol = Solution()
print(sol.maxAreaOfIsland([[0, 0, 0, 0, 0, 0, 0, 0]]))
print(sol.maxAreaOfIsland([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]))
print(sol.maxAreaOfIsland([
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
]))
