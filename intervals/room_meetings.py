from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return  self.start < other.start

class Solution:
    def overlap(self, interval1: Interval, interval2 : Interval):

        if interval2.start > interval1.end or interval2.end < interval1.start:
            return False

        return True


    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort()
        for i in range(1,len(intervals)):
            if self.overlap(intervals[i-1],intervals[i]):
                return False

        return True


s = Solution()
print(s.canAttendMeetings(intervals = [Interval(5,8),Interval(9,15)]))

