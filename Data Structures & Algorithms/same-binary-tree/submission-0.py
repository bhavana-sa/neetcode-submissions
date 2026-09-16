# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: #If both nodes are None, they are the same, so we return True
            return True

        if p and q and p.val == q.val: #Does node p exist?Does node q exist? Do their values match?
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) #We recursively compare: p.left  with q.left AND p.right with q.right. Both sides must be True.
        else:
            return False
        