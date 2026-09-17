# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root #The node we're currently examining.

        while cur: #Keep going while cur exists.
            if p.val > cur.val and q.val > cur.val: #This asks: Are BOTH p and q greater than the current node?
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val: #Are BOTH p and q smaller than the current node?
                cur = cur.left
            else:
                return cur
        
        #If both p and q are smaller, go left. If both are larger, go right. Otherwise, we've found the LCA.
        #left subtree < node < right subtree -> Binary Search tree