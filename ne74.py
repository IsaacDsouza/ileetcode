#74. Search a 2D Matrix. You are given an m x n integer matrix matrix with the following two properties: Each row is sorted in non-decreasing order.   The first integer of each row is greater than the last integer of the previous row. Given an integer target, return true if target is in matrix or false otherwise. You must write a solution in O(log(m * n)) time complexity.
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows-1
        row=-1

        while top<=bottom:
            mid = (top+bottom)//2
            if matrix[mid][0]<=target<=matrix[mid][-1]:
                row=mid
            elif target<matrix[mid][0]:
                bottom=mid-1
            else:
                top=mid+1
        if row==-1:
            return False

        l,r = 0, cols-1
        while l<=r:
            m=(l+r)//2
            if matrix[row][m]==target:
                return True
            elif target < matrix[row][m]:
                r=m-1
            else:
                l=m+1
        return False

solution = Solution()
print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))


        