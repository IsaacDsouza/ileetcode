#994. Rotting Oranges. You are given an m x n grid where each cell can have one of three values: representing an empty cell, representing a fresh orange, representing a rotten orange. Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        time, fresh = 0,0
        q=deque()
        m,n=len(grid), len(grid[0])

        for r in range(m):
            for c in range(n):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    q.append([r,c])
        dir=[[0,1],[1,0],[0,-1],[-1,0]]
        while q and fresh>0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dir:
                    row, col = r+dr,c+dc
                    if row<0 or row==m or col<0 or col==n or grid[row][col]!=1:
                        continue
                    grid[row][col]=2
                    q.append([row, col])
                    fresh-=1
            time+=1
        return time if fresh==0 else -1
    
solution=Solution()
print(solution.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))