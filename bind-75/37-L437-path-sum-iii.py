'''
437. Path Sum III
https://leetcode.com/problems/path-sum-iii/description/?envType=study-plan-v2&envId=leetcode-75

Given the root of a binary tree and an integer targetSum, return the number of paths
where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf,
but it must go downwards (i.e., traveling only from parent nodes to child nodes).

--
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.
'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node: Optional[TreeNode], cumulative_sums: dict, current_sum: int) -> int:
            if node is None: return 0

            # Update the current path sum
            current_sum += node.val

            # Check if there exists a prefix path (anywhere above) whose sum,
            # when subtracted from current_sum, equals targetSum
            path_count = cumulative_sums.get(current_sum - targetSum, 0)

            # Include this current path sum in cumulative sums
            cumulative_sums[current_sum] = cumulative_sums.get(current_sum, 0) + 1

            # Recursive DFS to child nodes with updated cumulative sums
            path_count += dfs(node.left, cumulative_sums, current_sum)
            path_count += dfs(node.right, cumulative_sums, current_sum)

            # Backtrack: remove the current path sum count for this path when returning
            cumulative_sums[current_sum] -= 1

            return path_count

        # Start DFS with an empty cumulative sum dictionary
        return dfs(root, {0: 1}, 0)


def run_tests():
    sol = Solution()

    # Test Case 1
    # Tree:       10
    #            /  \
    #           5   -3
    #          / \    \
    #         3   2    11
    #        / \   \
    #       3  -2   1
    # Paths that sum to 8: [5, 3], [5, 3, -2, 1], [10, -3, 11]
    root1 = TreeNode(10)
    root1.left = TreeNode(5)
    root1.right = TreeNode(-3)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(2)
    root1.right.right = TreeNode(11)
    root1.left.left.left = TreeNode(3)
    root1.left.left.right = TreeNode(-2)
    root1.left.right.right = TreeNode(1)
    assert sol.pathSum(root1, 8) == 3

    # Test Case 2
    # Tree:       1
    # Paths that sum to 1: [1]
    root2 = TreeNode(1)
    assert sol.pathSum(root2, 1) == 1

    # Test Case 3
    # Tree is empty, so no paths
    root3 = None
    assert sol.pathSum(root3, 8) == 0

    # Test Case 4
    # Tree:       1
    #            / \
    #           1   1
    # Paths that sum to 2: [1, 1], [1, 1]
    root4 = TreeNode(1)
    root4.left = TreeNode(1)
    root4.right = TreeNode(1)
    assert sol.pathSum(root4, 2) == 2

    # Test Case 5: Includes both positive and negative numbers and tests zero as the target sum.
    # Tree:       0
    #            / \
    #           1  -1
    # Paths that sum to 0: [0], [0, 1, -1]
    root5 = TreeNode(0)
    root5.left = TreeNode(1)
    root5.right = TreeNode(-1)
    assert sol.pathSum(root5, 0) == 1

    print("All test cases passed.")

run_tests()