# Author aw.ahmed.werghi@gmail.com
# problem statement : https://leetcode.com/problems/find-peak-element/description/



class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        if len(nums) == 1 : return 0
        while True :
            mid = (start + end) // 2
            if nums[mid] > nums[mid-1] and mid == len(nums) - 1:
                return len(nums) - 1
            elif nums[mid] > nums[mid+1] and mid == 0 :
                return 0
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
            elif nums[mid] < nums[mid+1]:
                start = mid + 1
            else :
                end = mid

s = Solution()
print(s.findPeakElement(nums=[1,2,3,1])) # output : answer : 2
print(s.findPeakElement(nums=[1,2,1,3,5,6,4])) # output : answer : 5