# 973. Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0). The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        points.sort(key=lambda x: x[0]**2 + x[1]**2)
        return points[:k]

solution = Solution()
print(solution.kClosest([[3,3],[5,-1],[-2,4]], 2))
print(solution.kClosest([[1,3],[-2,2]], 1))