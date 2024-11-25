'''
https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/?envType=study-plan-v2&envId=leetcode-75

You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

---
Example 1:

Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
Output: [4,0,3]
Explanation:
- 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
- 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
- 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
Thus, [4,0,3] is returned.
'''
from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        result, n = [], len(potions)
        potions.sort()  # Sort potions so we can perform binary search

        for spell in spells:
            lo, hi = 0, n

            # Binary Search
            while lo < hi:
                mid = (lo + hi) // 2
                if spell * potions[mid] >= success:
                    hi = mid  # Narrow down to left side
                else:         # Narrow down to right side
                    lo = mid + 1

            # Low index now points to the first valid index
            result.append(n - lo)

        return result

# Time Complexity: 𝑂(𝑚 log 𝑚 + 𝑛 log 𝑚) | sorting+bs | m=len(potions), n=len(spells)
def run_tests():
    sol = Solution()

    t1 = sol.successfulPairs([5,1,3], [1,2,3,4,5], 7)
    assert t1 == [4,0,3]

    t2 = sol.successfulPairs([3,1,2], [8,5,8], 16)
    assert t2 == [2,0,2]

    t3 = sol.successfulPairs([1,2,3,4,5,6,7], [1,2,3,4,5,6,7], 25)
    assert t3 == [0,0,0,1,3,3,4]

    t3 = sol.successfulPairs([10,15,20], [1,2,3,4,5], 40)
    assert t3 == [2,3,4]

    print('All test cases passed.')

run_tests()