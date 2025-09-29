#1039. Minimum Score Triangulation of Polygon. You have a convex n-sided polygon where each vertex has an integer value. You are given an integer array values where values[i] is the value of the ith vertex in clockwise order. Polygon triangulation is a process where you divide a polygon into a set of triangles and the vertices of each triangle must also be vertices of the original polygon. Note that no other shapes other than triangles are allowed in the division. This process will result in n - 2 triangles. You will triangulate the polygon. For each triangle, the weight of that triangle is the product of the values at its vertices. The total score of the triangulation is the sum of these weights over all n - 2 triangles. Return the minimum possible score that you can achieve with some triangulation of the polygon


class Solution:
    def minScoreTriangulation(self, values: list[int]) -> int:
        n = len(values)
        if n < 3:
            return 0
        dp = [[0] * n for _ in range(n)]
        
        for length in range(3, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                best = float('inf')
                for k in range(i + 1, j):
                    cost = dp[i][k] + dp[k][j] + values[i] * values[k] * values[j]
                    if cost < best:
                        best = cost
                dp[i][j] = best
        return dp[0][n-1]
solution = Solution()
print(solution.minScoreTriangulation([3,7,4,5]))