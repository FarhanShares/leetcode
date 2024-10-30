'''
1448. Count Good Nodes in Binary Tree
https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75

Given a binary tree root, a node X in the tree is named good if in the path from root to X
there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

--
Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        queue = [(root, float('-inf'))]

        while queue:
            current, current_max = queue.pop(0)
            if current.val >= current_max: res += 1
            new_max = max(current_max, current.val)

            if current.left: queue.append((current.left, new_max))
            if current.right: queue.append((current.right, new_max))

        return res

def run_tests():
    # Test case 1
    root1 = TreeNode(3)
    root1.left = TreeNode(1)
    root1.right = TreeNode(4)
    root1.left.left = TreeNode(3)
    root1.right.left = TreeNode(1)
    root1.right.right = TreeNode(5)
    print("Test case 1 -> Expected output: 4 -> Result:", Solution().goodNodes(root1))

    # Test case 2
    root2 = TreeNode(3)
    root2.left = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(2)
    print("Test case 2 -> Expected output: 3 -> Result:", Solution().goodNodes(root2))

    # Test case 3 (Edge case: single node)
    root3 = TreeNode(1)
    print("Test case 3 -> Expected output: 1 -> Result:", Solution().goodNodes(root3))


run_tests()