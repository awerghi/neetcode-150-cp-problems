import heapq
from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # map to capture items occurences
        map_occ = defaultdict(int)

        for elt in nums:
            map_occ[elt] += 1

        heap = []
        for num,freq in map_occ.items():
            heapq.heappush(heap,(freq,num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for (freq,num) in heap]

s = Solution()
print(s.topKFrequent([1,2,2,3,3,3],2))