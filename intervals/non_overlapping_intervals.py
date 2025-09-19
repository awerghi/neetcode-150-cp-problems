from typing import List

class Solution:
    def interval_overlap(self, interval : List[int], other_interval : List[int]) -> bool:
        start,end = interval
        other_start,other_end = other_interval

        if other_start >= end or other_end <= start:
            return False

        return True

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        new_intervals = [intervals[0]]
        for i in range(1,len(intervals)):
            if self.interval_overlap(new_intervals[-1],intervals[i]):
                continue
            else :
                new_intervals.append(intervals[i])

        return len(intervals) - len(new_intervals)


s = Solution()
print(s.eraseOverlapIntervals([[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]))
