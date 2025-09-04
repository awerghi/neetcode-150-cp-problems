from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        if len(nums) == 1: return nums[0]
        dp_products = [[nums[0]]]
        max_product = 0
        for i in range(1, len(nums)):
            aux = [nums[i]]
            for k in range(len(dp_products[i - 1])):
                if nums[i] > max_product: max_product = nums[i]
                if nums[i] * dp_products[i - 1][k] > max_product:
                    max_product = nums[i] * dp_products[i - 1][k]
                aux.append(nums[i] * dp_products[i - 1][k])
            dp_products.append(aux)

        return max_product
