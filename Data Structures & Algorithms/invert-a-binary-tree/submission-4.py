from collections import deque #This line imports deque from Python's built-in collections module.

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = root.right, root.left #This swaps the left and right children.

        self.invertTree(root.left)  #I inverted the current node. Now I need to invert the entire left subtree.
        self.invertTree(root.right) #I inverted the current node. Now I need to invert the entire right subtree.

        return root


#recursion DFS
