#118. Pascal's Triangle. Given an integer numRows, return the first numRows of Pascal's triangle. In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        pascal=[]

        for i in range(numRows):
            row=[1]*(i+1)
            for j in range(1, i):
                row[j]=pascal[i-1][j-1]+pascal[i-1][j]
            pascal.append(row)
        return pascal

solution  = Solution()
print(solution.generate(5))