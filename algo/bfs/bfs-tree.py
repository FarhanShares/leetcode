class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bfs_tree(root):
    if not root:
        return

    queue = [root]  # Initialize a queue with the root node

    while queue:
        current = queue.pop(0)  # Dequeue the current node
        print(current.val)  # Process the current node

        if current.left:
            queue.append(current.left)  # Enqueue the left child
        if current.right:
            queue.append(current.right)  # Enqueue the right child

# Example usage:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

bfs_tree(root)  # Traverses and prints the tree nodes in BFS order -> Output: 1,2,3,4,5