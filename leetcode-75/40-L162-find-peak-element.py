'''
https://leetcode.com/problems/find-peak-element/description/?envType=study-plan-v2&envId=leetcode-75

A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index.
If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered
to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

---
Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2,
or index number 5 where the peak element is 6.
'''
from typing import List


class Solution:
     def findPeakElement(self, nums: List[int]) -> int:
        k = len(nums)
        if k == 1: return 0

        lo, hi = 0, k-1

        while lo < hi:
            mid = (lo + hi) // 2

            if nums[mid] > nums[mid+1]:
                hi = mid   # move left since next element is greater
            else:
                lo = mid+1 # move right as previous element is smaller

        return lo

# Time Complexity: 𝑂(lon n) | bs | n=len(nums)
# Intuition:
# * Though the array isn't sorted, we are guaranteed to have sorted local order, which
# * allow us to decide the direction to move, just like in a sorted array.
# * A peak is guaranteed, and binary search systematically narrows the range to find it.
# * Also the asking of making it O(log n) gives a hint to it.

def run_tests():
    sol = Solution()

    t1 = sol.findPeakElement([1,2,3,1])
    assert t1 == 2

    t2 = sol.findPeakElement([1,2,1,3,5,6,4])
    assert t2 == 5

    t3 = sol.findPeakElement([1])
    assert t3 == 0

    t3 = sol.findPeakElement([0,1,2])
    assert t3 == 2

    print('All test cases passed.')

run_tests()