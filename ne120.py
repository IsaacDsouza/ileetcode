#120. Triangle. Given a triangle array, return the minimum path sum from top to bottom. For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        memo={}

        def dfs(i,j):
            if i==len(triangle):
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            lower_left=triangle[i][j]+dfs(i+1,j)
            lower_right=triangle[i][j]+dfs(i+1, j+1)
            memo[(i,j)]=min(lower_left, lower_right)
            return memo[(i,j)]
        return dfs(0,0)
solution  = Solution()    
print(solution.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))