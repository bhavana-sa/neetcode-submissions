# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: #If there's no node:None the depth is:0 This is your base case.
            return 0

        left = self.maxDepth(root.left) #"What is the maximum depth of the left subtree?"
        right = self.maxDepth(root.right) #What is the maximum depth of the right subtree?"

        return 1 + max(left,right) #Take whichever subtree is deeper.Add 1 for the current node.means:"My depth is 1 for myself plus the deeper of my two subtrees." the depth of a node includes the current node itself.
        