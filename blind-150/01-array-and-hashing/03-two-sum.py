from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {} # store the diffs
        for i, num in enumerate(nums):
            complement = target - num

            if complement in complements:
                return [complements[complement], i]

            complements[num] = i
        return [-1, -1]

    def twoSumNonOptimized(self, nums: List[int], target: int) -> List[int]:
        # not the efficient way, let's just do it first
        for i in range(len(nums)):
            diff = target - nums[i]

            for j in range(i+1, len(nums)):
                print(f'i, j & diff is {i}  {j} {diff}')
                if(diff == nums[j]):
                    return [i, j]
        return [-1, -1] # just to make the linter happy even if it is guaranteed to have one solution


print(Solution().twoSum([2,7,11,15], 9))
print(Solution().twoSum([3,2,4], 6))