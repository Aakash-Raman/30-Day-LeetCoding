def findisland(grid, i, j):
        if(i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == '0'):
            return False
        grid[i][j] = '0'
        findisland(grid,i+1,j) # Up
        findisland(grid,i-1,j) # Down
        findisland(grid,i,j-1) # Left
        findisland(grid,i,j+1) # Right
    
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(0,len(grid)):
            for j in range(0,len(grid[i])):
                if(grid[i][j] == '1'):
                    count += 1
                    findisland(grid, i, j)
        return count            
    
    
