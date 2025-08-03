#3169. Count Days Without Meetings. You are given a positive integer days representing the total number of days an employee is available for work (starting from day 1). You are also given a 2D array meetings of size n where, meetings[i] = [start_i, end_i] represents the starting and ending days of meeting i (inclusive). Return the count of days when the employee is available for work but no meetings are scheduled. Note: The meetings may overlap.

class Solution:
    def countDays(self, days: int, meetings: list[list[int]]) -> int:
        meetings.sort(key = lambda i:i[0])
        merged=[]

        for meeting in meetings:
            if not merged or merged[-1][1]<meeting[0]:
                merged.append(meeting)
            else:
                merged[-1]=[merged[-1][0], max(merged[-1][1], meeting[1])]
        
        res=merged[0][0]-1
        for i in range(len(merged)-1):
            res+=merged[i+1][0]-merged[i][1]-1
        if days-merged[-1][1]==0:
            return res
        res+=(days-merged[-1][1])
        return res

solution = Solution()
print(solution.countDays(10, [[5,7],[1,3],[9,10]]))