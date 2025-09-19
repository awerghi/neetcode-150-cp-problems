from typing import List


class Solution:
    def interval_overlap(self,interval : List[int], other_interval: List[int]):
        start,end = interval
        other_start,other_end = other_interval

        if other_start > end or other_end < start:
            return False

        return True

    def merge_two_overlaping_intervals(self,interval : List[int] , other_interval : List[int]):
        start,end = interval
        other_start, other_end = other_interval

        return [start,max(end,other_end)]

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x : x[0])
        new_intervals = [intervals[0]]
        for i in range(1,len(intervals)):
            if self.interval_overlap(intervals[i],new_intervals[-1]):
                new_interval = self.merge_two_overlaping_intervals(new_intervals[-1],intervals[i])
                new_intervals.pop()
                new_intervals.append(new_interval)
            else :
                new_intervals.append(intervals[i])
        return new_intervals

s = Solution()
print(s.merge([[1,3],[1,5],[6,7]]))
print(s.merge([[1,2],[2,3]]))
print(s.merge([[1,2]]))