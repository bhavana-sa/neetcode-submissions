# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True

            if not (left < node.val < right):
                return False

            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        return valid(root, float("-inf"), float("inf"))

#
# VALID BST:
#
#             5
#           /   \
#          3     8
#         / \   / \
#        1   4 7   9
#
#
# BST RULE:
#
# Everything on the LEFT  < current node
# Everything on the RIGHT > current node
#
#
# The helper function:
#
#     valid(node, left, right)
#
# means:
#
#     "Is this node valid between the boundaries
#      left and right?"
#
#
# IMPORTANT:
#
# node = current node we are checking
# left = minimum allowed value
# right = maximum allowed value
#
#
# =========================================================
# STEP 1: INITIAL CALL
# =========================================================
#
# return valid(root, float("-inf"), float("inf"))
#
# root = 5
#
# So:
#
# valid(
#     node = 5,
#     left = -inf,
#     right = +inf
# )
#
# Think:
#
#     5 is allowed to be anywhere between
#     -infinity and +infinity.
#
#
# ---------------------------------------------------------
# Inside valid(5, -inf, +inf)
# ---------------------------------------------------------
#
# if not node:
#
# node = 5 → node exists
# → condition is False
#
#
# if not (left < node.val < right):
#
# Check:
#
#     -inf < 5 < +inf
#
# True
#
# So 5 is valid.
#
#
# Now:
#
# return valid(node.left, left, node.val) AND
#        valid(node.right, node.val, right)
#
#
# For LEFT child:
#
#     valid(3, -inf, 5)
#
# For RIGHT child:
#
#     valid(8, 5, +inf)
#
#
# =========================================================
# STEP 2: CHECK NODE 3
# =========================================================
#
# Call:
#
#     valid(
#         node = 3,
#         left = -inf,
#         right = 5
#     )
#
# Why right = 5?
#
# Because 3 is the LEFT child of 5.
#
# Therefore:
#
#     3 must be < 5
#
#
# Check:
#
#     -inf < 3 < 5
#
# True
#
# So node 3 is valid.
#
#
# Now check its children.
#
#
# LEFT child of 3:
#
#     valid(1, -inf, 3)
#
# RIGHT child of 3:
#
#     valid(4, 3, 5)
#
#
# =========================================================
# STEP 3: CHECK NODE 1
# =========================================================
#
# Call:
#
#     valid(
#         node = 1,
#         left = -inf,
#         right = 3
#     )
#
# Why right = 3?
#
# Because 1 is the LEFT child of 3.
#
# Therefore:
#
#     1 must be < 3
#
#
# Check:
#
#     -inf < 1 < 3
#
# True
#
# Node 1 is valid.
#
#
# Node 1 has no children:
#
#     valid(None, -inf, 1)
#         → True
#
#     valid(None, 1, 3)
#         → True
#
#
# Therefore:
#
#     valid(1, -inf, 3)
#         → True
#
#
# =========================================================
# STEP 4: CHECK NODE 4
# =========================================================
#
# Call:
#
#     valid(
#         node = 4,
#         left = 3,
#         right = 5
#     )
#
# Why?
#
# 4 is:
#     RIGHT of 3
#     AND
#     LEFT of 5
#
# Therefore 4 must satisfy BOTH:
#
#     4 > 3
#     4 < 5
#
#
# Check:
#
#     3 < 4 < 5
#
# True
#
# Node 4 is valid.
#
#
# Node 4 has no children:
#
#     valid(None, 3, 4)
#         → True
#
#     valid(None, 4, 5)
#         → True
#
#
# Therefore:
#
#     valid(4, 3, 5)
#         → True
#
#
# =========================================================
# STEP 5: FINISH NODE 3
# =========================================================
#
# We have:
#
#     valid(1, -inf, 3) → True
#
# AND
#
#     valid(4, 3, 5) → True
#
#
# Therefore:
#
#     valid(3, -inf, 5)
#
#     = True AND True
#
#     = True
#
#
# =========================================================
# STEP 6: CHECK NODE 8
# =========================================================
#
# Now we return to the root 5 and check its RIGHT child.
#
# Call:
#
#     valid(
#         node = 8,
#         left = 5,
#         right = +inf
#     )
#
# Why left = 5?
#
# Because 8 is the RIGHT child of 5.
#
# Therefore:
#
#     8 must be > 5
#
#
# Check:
#
#     5 < 8 < +inf
#
# True
#
# Node 8 is valid.
#
#
# Now check its children.
#
#
# LEFT child of 8:
#
#     valid(7, 5, 8)
#
# RIGHT child of 8:
#
#     valid(9, 8, +inf)
#
#
# =========================================================
# STEP 7: CHECK NODE 7
# =========================================================
#
# Call:
#
#     valid(
#         node = 7,
#         left = 5,
#         right = 8
#     )
#
# 7 is:
#     RIGHT of 5
#     AND
#     LEFT of 8
#
# Therefore:
#
#     5 < 7 < 8
#
# True
#
# Node 7 is valid.
#
#
# Node 7 has no children:
#
#     valid(None, 5, 7) → True
#     valid(None, 7, 8) → True
#
#
# Therefore:
#
#     valid(7, 5, 8) → True
#
#
# =========================================================
# STEP 8: CHECK NODE 9
# =========================================================
#
# Call:
#
#     valid(
#         node = 9,
#         left = 8,
#         right = +inf
#     )
#
# Check:
#
#     8 < 9 < +inf
#
# True
#
# Node 9 is valid.
#
#
# Node 9 has no children:
#
#     valid(None, 8, 9) → True
#     valid(None, 9, +inf) → True
#
#
# Therefore:
#
#     valid(9, 8, +inf) → True
#
#
# =========================================================
# STEP 9: FINISH NODE 8
# =========================================================
#
# We have:
#
#     valid(7, 5, 8) → True
#
# AND
#
#     valid(9, 8, +inf) → True
#
#
# Therefore:
#
#     valid(8, 5, +inf)
#
#     = True AND True
#
#     = True
#
#
# =========================================================
# STEP 10: FINISH ROOT NODE 5
# =========================================================
#
# We have:
#
# LEFT subtree:
#
#     valid(3, -inf, 5) → True
#
# RIGHT subtree:
#
#     valid(8, 5, +inf) → True
#
#
# Therefore:
#
#     valid(5, -inf, +inf)
#
#     = True AND True
#
#     = True
#
#
# FINAL ANSWER:
#
#     True
#
#
# =========================================================
# THE MOST IMPORTANT IDEA
# =========================================================
#
# Every node gets a RANGE of allowed values.
#
#
# ROOT:
#
#     5
#     range = (-inf, +inf)
#
#
# GO LEFT FROM 5:
#
#     3
#     range = (-inf, 5)
#
#
# GO RIGHT FROM 5:
#
#     8
#     range = (5, +inf)
#
#
# GO LEFT FROM 8:
#
#     7
#     range = (5, 8)
#
#
# GO RIGHT FROM 3:
#
#     4
#     range = (3, 5)
#
#
# So remember:
#
#     GO LEFT:
#         right boundary becomes current node
#
#         valid(node.left, left, node.val)
#
#
#     GO RIGHT:
#         left boundary becomes current node
#
#         valid(node.right, node.val, right)
#
#
# =========================================================
# INVALID EXAMPLE
# =========================================================
#
#             5
#              \
#               8
#              /
#             4
#
#
# Start:
#
#     valid(5, -inf, +inf)
#         → valid
#
#
# Go RIGHT:
#
#     valid(8, 5, +inf)
#         → valid
#
#
# Go LEFT from 8:
#
#     valid(4, 5, 8)
#
# Why is the left boundary still 5?
#
# Because 4 is STILL inside the right subtree of 5.
#
# Therefore 4 must be:
#
#     greater than 5
#     AND
#     less than 8
#
# Check:
#
#     5 < 4 < 8
#
# False
#
# Therefore:
#
#     return False
#
# The tree is NOT a valid BST.
#
#
# =========================================================
# COMPLEXITY
# =========================================================
#
# n = number of nodes
#
# Time: O(n)
#
# Every node is visited once.
#
# Space: O(h)
#
# h = height of the tree.
#
# Balanced tree:
#     O(log n)
#
# Worst-case skewed tree:
#     O(n)
#
#
# =========================================================
# INTERVIEW MEMORY TRICK
# =========================================================
#
# BST VALIDATION:
#
#     Every node must stay inside its allowed range.
#
#     LEFT  → upper bound becomes current node
#     RIGHT → lower bound becomes current node
#
#     left < node.val < right
#
# =========================================================