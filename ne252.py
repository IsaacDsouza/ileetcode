#252. Meeting Rooms. Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), determine if a person could add all meetings to their schedule without any conflicts.



class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        if len(intervals)<=1:
            return True
        intervals.sort(key=lambda i:i.start)

        for i in range(len(intervals)-1):
            if intervals[i].end > intervals[i+1].start:
                return False
        return True

solution = Solution()
print(solution.canAttendMeetings([(0,30),(5,10),(15,20)]))

        