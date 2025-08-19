# PROBLEM STATEMENT : https://neetcode.io/problems/merge-sorted-array?list=neetcode250
# Author aw.aw.ahmed.werghi@gmail.com

class Solution:
    def move_array_by_one(self, nums: List[int], start: int, end: int, elt: int):
        # we will move the array supposing there is free space at the end of the array
        for i in range(end, start - 1, -1):
            nums[i + 1] = nums[i]
        nums[start] = elt

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(n):
            ok = False
            for j in range(m):
                if nums2[i] < nums1[j]:
                    self.move_array_by_one(nums1, j, m - 1, nums2[i])
                    m += 1
                    ok = True
                    break
                else:
                    continue
            if not ok:
                nums1[m] = nums2[i]
                m += 1
