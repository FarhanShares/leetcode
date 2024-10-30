class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs_recursive(node):
    if not node: return

    print(node.val)  # Process the current node

    dfs_recursive(node.left)  # Recursively visit left subtree
    dfs_recursive(node.right)  # Recursively visit right subtree

def dfs_iterative(root):
    if not root:
        return

    stack = [root]  # Initialize stack with the root node
    while stack:
        node = stack.pop()  # Pop the last node added to the stack
        print(node.val)  # Process the current node

        # Push right child first so left child is processed first
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)

# Example usage
# Construct a sample binary tree
#       1
#      / \
#     2   3
#    / \
#   4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Call the recursive DFS
dfs_recursive(root) # 1, 2, 4, 5, 3
print("---")
# Call the iterative DFS
dfs_iterative(root) # 1, 2, 4, 5, 3