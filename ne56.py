#56. Merge Intervals. Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda interval: interval[0])
        merged = []
        
        prev = intervals[0]
        for interval in intervals:
            if interval[0]<=prev[1]:
                prev[1]=max(prev[1], interval[1])
            else:
                merged.append(prev)
                prev=interval
            
        return merged

solution = Solution()
print(solution.merge([[1,3],[2,6],[8,10],[15,18]]))