#56. Merge Intervals. Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda interval: interval[0])
        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1]= [ merged[-1][0], max(merged[-1][1], interval[1])]
        return merged

solution = Solution()
print(solution.merge([[1,3],[2,6],[8,10],[15,18]]))