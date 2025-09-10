from typing import List

class Solution:

    def search_rotation_index(self, nums: List[int]) -> int:
        n = len(nums)
        start = 0
        end = n - 1

        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid
            else :
                end = mid

            if nums[mid] > nums[mid + 1]:
                return mid + 1
        return n


    def binary_search(self,nums,target):

        n = len(nums) - 1
        if n == 0 and nums[0] == target:
            return 0
        elif n == 0:
            return -1

        start = 0
        end = n

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return -1

    def search(self, nums: List[int], target: int) -> int:
        rotation_index = self.search_rotation_index(nums)
        nums = nums[rotation_index:] + nums[:rotation_index]
        target_index = self.binary_search(nums,target)
        if target_index != -1:
            return (target_index + rotation_index) % len(nums)
        else :
            return -1





s = Solution()
print(s.search(nums = [3,5,6,0,1,2], target = 4))