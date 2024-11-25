from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        most = 0
        lft, rht = 0, len(height)-1

        while lft < rht:
            x, y = height[lft], height[rht]
            # h=shorter one is the height, w=indices distance is the width
            # h=shorter: or water will overflow, w=distance: of the two bars
            h, w = min(x, y), rht-lft
            most = max(most, h * w)

            if x < y:
                lft += 1
            else:
                rht -= 1

        return most

        # BRUTE FORCE
        # res = 0

        # for l in range (len(height)):
        #     for r in range(l+1, len(height)):
        #         # x-axis calculation of width
        #         x = r - l
        #         # y-axis, take the lowest otherwise water spills
        #         y = min(height[l], height[r])
        #         res = max(res, x * y)

        # return res

        # TWO POINTERS LEANEAR TIME SOLUTION
        res = 0
        l, r = 0, len(height) - 1

        while l < r:
            # x-axis width calculation
            x = r - l
            # y-axis height, take the lowest otherwise water will spill out
            y = min(height[l], height[r])
            # update the result with max value
            res = max(res, x * y)

            # move the shorter line towards the center
            if height[l] < height[r]: l += 1
            else: r -= 1
        return res