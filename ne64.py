#64. Minimum Path Sum. Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path. Note: You can only move either down or right at any point in time.

class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        memo={}

        def dfs(i,j,memo):
            if (i,j) in memo:
                return memo[(i,j)]

            if i<0 or j<0:
                return float('inf')
            
            if i==0 and j==0:
                return grid[i][j]
            
            result=min(dfs(i,j-1,memo), dfs(i-1,j,memo))+grid[i][j]
            memo[(i,j)]=result
            return result
        return dfs(len(grid)-1, len(grid[0])-1,memo)

solution  = Solution()
print(solution.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
            
