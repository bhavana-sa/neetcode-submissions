# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: #If subRoot is empty:subRoot = None then technically an empty tree is considered a subtree.
            return True
        if not root: #if root is none, There is nowhere for subRoot to exist.
            return False

        if self.isSametree(root, subRoot): #Could subRoot start at this exact node? if it is true, then we are done. this is our answer
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) #If not, search left and right

    def isSametree(self, root: Optional[Treenode], subRoot:Optional[Treenode]) -> bool: #Are these two trees exactly identical?
        if not root and not subRoot: #Both nodes are empty, same tree noo
            return True
        if root and subRoot and root.val == subRoot.val: #This checks:root exists, subRoot exists, Their values are equal, If all three are true, compare their children
            return self.isSametree(root.left, subRoot.left) and self.isSametree(root.right, subRoot.right)



# ---------------------------------------------------------
#
# Start:
#
# isSubtree(root=3, subRoot=4)
#
# MAIN TREE current node = 3
# SUBTREE root            = 4
#
# if not subRoot:
#     subRoot is 4 → not None → False
#
# if not root:
#     root is 3 → not None → False
#
# if self.sameTree(root, subRoot):
#     Call:
#
#     sameTree(root=3, subRoot=4)
#
#
# ---------------------------------------------------------
# STEP 2: sameTree(3, 4)
# ---------------------------------------------------------
#
# Here:
#     root    = 3  ← MAIN TREE
#     subRoot = 4  ← SUBTREE
#
# if not root and not subRoot:
#     3 and 4 both exist → False
#
# if root and subRoot and root.val == subRoot.val:
#     3 == 4 → False
#
# return False
#
# Therefore:
#
# sameTree(3, 4) → False
#
#
# ---------------------------------------------------------
# STEP 3
# ---------------------------------------------------------
#
# We return to:
#
# isSubtree(root=3, subRoot=4)
#
# Since sameTree(3,4) was False, we execute:
#
# isSubtree(root.left, subRoot)
#
# root.left of MAIN TREE node 3 = 4
#
# So we call:
#
# isSubtree(root=4, subRoot=4)
#
#
# ---------------------------------------------------------
# STEP 4
# ---------------------------------------------------------
#
# Now:
#
# root    = 4  ← MAIN TREE
# subRoot = 4  ← SUBTREE
#
# Both are not None.
#
# Call:
#
# sameTree(root=4, subRoot=4)
#
#
# ---------------------------------------------------------
# STEP 5: sameTree(4, 4)
# ---------------------------------------------------------
#
# root    = 4  ← MAIN TREE
# subRoot = 4  ← SUBTREE
#
# Both exist.
#
# root.val == subRoot.val
#
# 4 == 4 → True
#
# Therefore we compare BOTH children:
#
# sameTree(root.left, subRoot.left)
# AND
# sameTree(root.right, subRoot.right)
#
#
# ---------------------------------------------------------
# STEP 6: Compare LEFT children
# ---------------------------------------------------------
#
# MAIN TREE left child of 4 = 1
# SUBTREE left child of 4    = 1
#
# Call:
#
# sameTree(root=1, subRoot=1)
#
# 1 == 1 → True
#
# Now compare their children:
#
# sameTree(None, None) → True
# sameTree(None, None) → True
#
# Therefore:
#
# sameTree(1, 1)
# = True AND True
# = True
#
#
# ---------------------------------------------------------
# STEP 7: Compare RIGHT children
# ---------------------------------------------------------
#
# MAIN TREE right child of 4 = 2
# SUBTREE right child of 4    = 2
#
# Call:
#
# sameTree(root=2, subRoot=2)
#
# 2 == 2 → True
#
# Compare their children:
#
# sameTree(None, None) → True
# sameTree(None, None) → True
#
# Therefore:
#
# sameTree(2, 2)
# = True AND True
# = True
#
#
# ---------------------------------------------------------
# STEP 8: Return from sameTree(4, 4)
# ---------------------------------------------------------
#
# We now have:
#
# LEFT subtree:
# sameTree(1,1) → True
#
# RIGHT subtree:
# sameTree(2,2) → True
#
# Therefore:
#
# sameTree(4,4)
# = True AND True
# = True
#
#
# ---------------------------------------------------------
# STEP 9: Return from isSubtree(4, 4)
# ---------------------------------------------------------
#
# We had:
#
# if self.sameTree(root, subRoot):
#
# sameTree(4,4) → True
#
# Therefore:
#
# return True
#
# We found the subtree!
#
#
# FINAL ANSWER:
#
# isSubtree(3,4) → True



        