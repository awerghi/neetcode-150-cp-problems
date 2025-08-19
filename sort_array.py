# Author aw.ahmed.werghi@gmail.com
# problem statement : https://neetcode.io/problems/sort-an-array?list=neetcode250


from typing import List

class Solution:
    def merge(self,nums:List[int],l:int,m:int,r:int):
        n1 = m - l + 1
        n2 = r - m

        # we should get the two parts of the array in order to reconstruct it
        nums1 = nums[l:m+1]
        nums2 = nums[m+1:r+1]

        i = 0
        j = 0
        # k point to the nums counter
        k = l

        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                nums[k] = nums1[i]
                i += 1
            else :
                nums[k] = nums2[j]
                j += 1
            k += 1
        # only one of the two following iterations will be executed
        # if it stills numbers in nums1
        for s in range(i,n1):
            nums[k] = nums1[s]
            k += 1

        # if it stills numbers in nums2
        for s in range(j,n2):
            nums[k] = nums2[s]
            k += 1

        return nums

    def mergeSort(self,nums,l,r):
        if l < r :
            middle = (l + r) // 2
            self.mergeSort(nums,l,middle)
            self.mergeSort(nums,middle+1,r)
            return self.merge(nums,l,middle,r)
        return [nums[l]]


    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums,0,len(nums)-1)

s = Solution()

# test cases
print(s.sortArray([10,9,1,1,1,2,3,1])) # -> [1, 1, 1, 1, 2, 3, 9, 10]
print(s.sortArray([5,10,2,1,3]))       # -> [1, 2, 3, 5, 10]
print(s.sortArray([1]))                # -> [1]