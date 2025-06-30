# 200. Number of Islands

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        m,n = len(grid), len(grid[0])
        def dfs(i, j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]!='1':
                return 
            else:
                grid[i][j]='0'
                dfs(i,j+1)
                dfs(i+1,j)
                dfs(i,j-1)
                dfs(i-1,j)
        islands=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    islands+=1
                    dfs(i,j)
        return islands
      

solution=Solution()
print(solution.numIslands([["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]]))

print(solution.numIslands([["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]]))
