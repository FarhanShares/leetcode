'''
1372. Longest ZigZag Path in a Binary Tree
https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75

You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
Change the direction from right to left or from left to right.
Repeat the second and third steps until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.

--

Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).
'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        return max(
            self.solver(root.left, isLeft = True, depth=0),
            self.solver(root.right,isLeft = False, depth=0),
        )


    # isLeft: the current direction
    def solver(self, node: Optional[TreeNode], isLeft: bool, depth: int) -> int:
        if not node:
            return depth

        if isLeft: # previously went left, go right
            depth = max(
                depth,
                self.solver(node.right, isLeft=False, depth=depth+1), # go right and increase depth
                self.solver(node.left, isLeft=True, depth=0), # go left, reset depth counter
            )
        else: # previously went right, go left
            depth = max(
                depth,
                self.solver(node.left, isLeft=True, depth=depth+1),
                self.solver(node.right, isLeft=False, depth=0),
            )
        return depth


def run_tests():
    sol = Solution()

    # Test case 1: Empty tree
    root1 = None
    assert sol.longestZigZag(root1) == 0  # No nodes, so longest zigzag path is 0

    # Test case 2: Single-node tree
    root2 = TreeNode(1)
    assert sol.longestZigZag(root2) == 0  # Only one node, no zigzag path

    # Test case 3: Tree with no zigzag paths
    # Tree structure:
    #     1
    #    /
    #   2
    #  /
    # 3
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.left.left = TreeNode(3)
    assert sol.longestZigZag(root3) == 1  # The longest zigzag path is 1

    # Test case 4: Tree with a clear zigzag path
    # Tree structure:
    #        1
    #       / \
    #      2   3
    #       \
    #        4
    #       /
    #      5
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.right = TreeNode(3)
    root4.left.right = TreeNode(4)
    root4.left.right.left = TreeNode(5)
    assert sol.longestZigZag(root4) == 3  # Zigzag: 1 -> 2 -> 4 -> 5
    print("All test cases passed.")

run_tests()
