#1631.  Path With Minimum Effort. You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort. A route's effort is the maximum absolute difference in heights between two consecutive cells of the route. Return the minimum effort required to travel from the top-left cell to the bottom-right cell.
import heapq
class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        rows, cols= len(heights), len(heights[0])
        minHeap=[[0,0,0]] #[[diff,r,c]]
        visit=set()
        dir=[[0,1], [-1,0], [0,1], [1,0]]

        while minHeap:
            diff, r, c = heapq.heappop(minHeap)

            if (r,c) in visit:
                continue
            visit.add((r,c))

            if (r,c)==(rows-1, cols-1):
                return diff
            
            for dr, dc in dir:
                newR, newC = r+dr, c+dc

                if (newR<0 or newC<0 or newR==rows or newC==cols or (newR, newC)in visit):
                    continue
                newDiff=max(diff, abs(heights[r][c]-heights[newR][newC]))
                heapq.heappush(minHeap,[newDiff, newR, newC])

solution = Solution()
print(solution.minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]))