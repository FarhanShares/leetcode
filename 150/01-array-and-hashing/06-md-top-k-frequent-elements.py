# https://leetcode.com/problems/top-k-frequent-elements/
# 347. Top K Frequent Elements
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count the chars
        hashMap = {}
        for _, n in enumerate(nums):
            hashMap[n] = 1 + hashMap.get(n, 0)

        # find the maximum frequency
        max_freq = max(hashMap.values())

        # modified bucket sort
        modSort = [[] for _ in range(max_freq + 1)]
        for num, freq in hashMap.items():
            modSort[freq].append(num)

        # get the most frequent items for k times
        res = []
        for i in range(len(modSort) - 1, -1, -1):
            if modSort[i] is not None:
                res.extend(modSort[i])
                if len(res) > k:
                    break
        return res[:k]

print(Solution().topKFrequent([1,2,3,1,1,2,2], 2))