# PROBLEM STATEMENT : https://neetcode.io/problems/three-integer-sum?list=neetcode150
# Author aw.ahmed.werghi@gmail.com




from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[List[int]]:
        i = 0
        j = len(numbers) - 1
        res_two_sum = []
        while i < j:
            if numbers[i] + numbers[j] == target:
                res_two_sum.append([numbers[i], numbers[j]])
                i += 1
                j -= 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1
        if res_two_sum:
            return res_two_sum
        return [[-1]]


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        three_sum_result = []
        for i in range(len(nums)):
            # get the list from current index + 1 in order to not get duplicates
            new_nums = nums[i+1:]
            new_nums.sort()
            # search for the negative of the current number using two sum feature
            res_new_nums = self.twoSum(new_nums,-1 * nums[i])
            if res_new_nums == [[-1]]:
                continue
            else :
                for elt in res_new_nums:
                    elt.append(nums[i])
                    elt.sort()
                    if elt not in three_sum_result:
                        three_sum_result.append(elt)
        return three_sum_result


s = Solution()
print(s.threeSum([-2,0,1,1,2]))