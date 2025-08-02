# Author ahmed.werghi@gmail.com

# My implementation of a merge sort

class Solution:
    def merge(self,nums,l1,l2,r1,r2):
        aux1 = nums[l1:r1+1]
        aux2 = nums[l2:r2+1]
        i = 0
        j = 0
        k = 0
        n = min(len(aux1),len(aux2))
        while i < n and j < n :
            if aux1[i] < aux2[j]:
                nums[l1+k] = aux1[i]
                i += 1
            else :
                nums[l1 + k] = aux2[j]
                j += 1
            k += 1
        for i in range(i,len(aux1)):
            nums[l1+k] = aux1[i]
            k += 1
        for i in range(j,len(aux2)):
            nums[l1+k] = aux2[i]
            k += 1
        return nums


    def merge_sort(self,nums,start,end):
        if start == end :
            return [nums[start]]

        mid = (start + end) // 2
        self.merge_sort(nums,start,mid)
        self.merge_sort(nums,mid+1,end)
        return  self.merge(nums,start,mid+1,mid,end)


s = Solution()
nums = [1,7,9,2,6,18]
print(s.merge_sort(nums,0,5)) # output : [1,2,6,7,9,18]