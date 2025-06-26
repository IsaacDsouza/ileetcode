# 695. Max Area of Island

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        d=[(1,0),(0,1),(-1,0),(0,-1)]
        maxi=0
        def dfs(i,j):
            if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j]==1:
                grid[i][j]=0
                cnt=1
                for dr,dc in d:
                    nr,nc=i+dr,j+dc
                    cnt+=dfs(nr,nc)
                return cnt
            return 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    maxi=max(maxi,dfs(i,j))
        return maxi
        
solution=Solution()
print(solution.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))
print(solution.maxAreaOfIsland([0,0,0,0,0,0,0,0]))