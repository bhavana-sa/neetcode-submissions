# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr  = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right

# DRY RUN
#
# BST:
#
#         5
#        / \
#       3   7
#      / \ / \
#     1  4 6  8
#
# k = 3
#
# Inorder traversal of a BST gives values in sorted order:
# 1 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
#
# stack = []
# curr = 5
#
# --------------------------------------------------
# STEP 1: Go left from 5
# --------------------------------------------------
#
# curr = 5
# stack = []
#
# stack.append(5)
# stack = [5]
# curr = 5.left = 3
#
# curr = 3
# stack.append(3)
# stack = [5, 3]
# curr = 3.left = 1
#
# curr = 1
# stack.append(1)
# stack = [5, 3, 1]
# curr = 1.left = None
#
# Now curr is None.
# We reached the leftmost/smallest node: 1
#
# --------------------------------------------------
# STEP 2: Visit node 1
# --------------------------------------------------
#
# curr = stack.pop()
# curr = 1
# stack = [5, 3]
#
# k -= 1
# k = 2
#
# k != 0, so 1 is not the kth smallest.
#
# curr = curr.right
# curr = 1.right = None
#
# --------------------------------------------------
# STEP 3: Visit node 3
# --------------------------------------------------
#
# curr is None, but stack is not empty.
#
# curr = stack.pop()
# curr = 3
# stack = [5]
#
# k -= 1
# k = 1
#
# k != 0, so 3 is not the kth smallest.
#
# curr = curr.right
# curr = 3.right = 4
#
# --------------------------------------------------
# STEP 4: Explore node 4
# --------------------------------------------------
#
# curr = 4
#
# stack.append(4)
# stack = [5, 4]
#
# curr = 4.left = None
#
# --------------------------------------------------
# STEP 5: Visit node 4
# --------------------------------------------------
#
# curr = stack.pop()
# curr = 4
# stack = [5]
#
# k -= 1
# k = 0
#
# k == 0
#
# return curr.val
# return 4
#
# ANSWER = 4


#What does "smallest" mean?
#Look at all the numbers in the tree: 5, 3, 7, 1, 4, 6, 8
#Put them in increasing order: 1, 3, 4, 5, 6, 7, 8
#Now we can identify their positions:
#1st → 1, 2nd → 3, 3rd → 4, 4th → 5, 5th → 6, 6th → 7, 7th → 8
        