# 200. Number of Islands

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        d=[(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(i,j):
            if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j]=="1":
                grid[i][j]=0
                for dr,dc in d:
                    nr,nc=i+dr,j+dc
                    dfs(nr,nc)
        cnt=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    cnt+=1
                    dfs(i,j)
        return cnt

solution=Solution()
print(solution.numIslands([["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]]))

print(solution.numIslands([["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]]))
