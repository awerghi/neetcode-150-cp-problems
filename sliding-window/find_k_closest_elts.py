from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        diff_inf = float('inf')
        diff_res = []
        # sliding window from start to len - k
        for start in range(n-k+1):
            # sum all the differences between x and elt in the sliding window
            diffs_list = [abs(x - arr[elt]) for elt in range(start,start+k)]
            # if the sum of the diff is minimum, take it
            if sum(diffs_list) < diff_inf:
                diff_res = arr[start:start+k]
                diff_inf = sum(diffs_list)
            else :
                continue
        return diff_res

s = Solution()
print(s.findClosestElements([1,2,3,4,5,6,7,8,9],3,8)) # => output : [7, 8, 9]
print(s.findClosestElements([2,3,4],3,1))             # => output : [7, 8, 9]
