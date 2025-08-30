# Author aw.ahmed.werghi@gmail.com
# problem statement : https://neetcode.io/problems/permutations?list=neetcode150

from typing import List

class Solution:
    def build_permutations(self,num,permutation):
        permutations = []
        n = len(permutation)

        for i in range(n+1):
            new_permutation = [100 for _ in range(n + 1)]
            new_permutation[i] = num
            for j in range(n):
                for k in range(n+1):
                    if new_permutation[k] == 100:
                        new_permutation[k] = permutation[j]
                        break
            permutations.append(new_permutation)
        return permutations

    def permute(self, nums: List[int]) -> List[List[int]]:
        permutation_list = [[[nums[0]]]]
        for i in range(1,len(nums)):
            aux = permutation_list[i-1]
            permutation_aux = []
            for elt in aux:
                aux_elt = self.build_permutations(nums[i],elt)
                permutation_aux += aux_elt

            permutation_list.append(permutation_aux)

        return permutation_list[-1]


s = Solution()
#print(s.build_permutations(3,[2,1]))
print(s.permute([1,2,3,4]))







