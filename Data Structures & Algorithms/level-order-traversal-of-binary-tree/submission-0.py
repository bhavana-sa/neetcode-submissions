# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []

            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if level:
                res.append(level)

        return res


# =========================================================
# DRY RUN
# =========================================================
#
# TREE:
#
#             3
#           /   \
#          9     20
#               /  \
#              15   7
#
# Expected output:
#
# [[3], [9, 20], [15, 7]]
#
#
# IMPORTANT IDEA:
#
# We use BFS because the problem wants the tree
# LEVEL BY LEVEL.
#
# q = queue
# qLen = number of nodes currently in THIS level
# level = values belonging to THIS level
# res = final answer containing all levels
#
#
# =========================================================
# STEP 1: INITIALIZATION
# =========================================================
#
# res = []
#
# Nothing has been added yet.
#
# res = []
#
#
# q = collections.deque()
#
# Create an empty queue.
#
# q = []
#
#
# q.append(root)
#
# root is the node 3.
#
# q = [3]
#
#
# =========================================================
# STEP 2: FIRST WHILE LOOP — LEVEL 0
# =========================================================
#
# while q:
#
# q is [3], so q is NOT empty.
#
# Enter the loop.
#
#
# qLen = len(q)
#
# q = [3]
# len(q) = 1
#
# Therefore:
#
# qLen = 1
#
# IMPORTANT:
# qLen = 1 means there is ONE node in the current level.
#
# Current level:
#
# Level 0 → [3]
#
#
# level = []
#
# This will store values for ONLY the current level.
#
#
# =========================================================
# STEP 3: PROCESS LEVEL 0
# =========================================================
#
# for i in range(qLen):
#
# qLen = 1
#
# Therefore:
#
# for i in range(1):
#
# The loop runs ONE time.
#
#
# ---------------------------------------------------------
# First iteration
# ---------------------------------------------------------
#
# node = q.popleft()
#
# q = [3]
#
# Remove the first node:
#
# node = 3
# q = []
#
#
# if node:
#
# node = 3, so it exists.
#
#
# level.append(node.val)
#
# node.val = 3
#
# Therefore:
#
# level = [3]
#
#
# q.append(node.left)
#
# node 3's left child = 9
#
# q = [9]
#
#
# q.append(node.right)
#
# node 3's right child = 20
#
# q = [9, 20]
#
#
# We have now processed all qLen = 1 nodes
# from Level 0.
#
#
# if level:
#
# level = [3], so it is not empty.
#
# res.append(level)
#
# res = [[3]]
#
#
# =========================================================
# STEP 4: SECOND WHILE LOOP — LEVEL 1
# =========================================================
#
# Queue is now:
#
# q = [9, 20]
#
# while q:
#
# q is not empty, so continue.
#
#
# qLen = len(q)
#
# len([9, 20]) = 2
#
# Therefore:
#
# qLen = 2
#
# IMPORTANT:
# There are TWO nodes in the current level.
#
# Level 1 → [9, 20]
#
#
# level = []
#
#
# =========================================================
# STEP 5: PROCESS LEVEL 1
# =========================================================
#
# for i in range(qLen):
#
# qLen = 2
#
# Therefore:
#
# for i in range(2):
#
# The loop runs TWO times.
#
#
# ---------------------------------------------------------
# First iteration
# ---------------------------------------------------------
#
# node = q.popleft()
#
# q = [9, 20]
#
# Remove 9:
#
# node = 9
# q = [20]
#
#
# if node:
#
# 9 exists.
#
#
# level.append(node.val)
#
# level = [9]
#
#
# q.append(node.left)
#
# Node 9 has no left child:
#
# q.append(None)
#
# q = [20, None]
#
#
# q.append(node.right)
#
# Node 9 has no right child:
#
# q.append(None)
#
# q = [20, None, None]
#
#
# ---------------------------------------------------------
# Second iteration
# ---------------------------------------------------------
#
# node = q.popleft()
#
# q = [20, None, None]
#
# Remove 20:
#
# node = 20
# q = [None, None]
#
#
# if node:
#
# 20 exists.
#
#
# level.append(node.val)
#
# level = [9, 20]
#
#
# q.append(node.left)
#
# Node 20's left child = 15
#
# q = [None, None, 15]
#
#
# q.append(node.right)
#
# Node 20's right child = 7
#
# q = [None, None, 15, 7]
#
#
# We have now processed exactly qLen = 2 nodes:
#
# 9 and 20
#
# These were the nodes belonging to Level 1.
#
#
# =========================================================
# STEP 6: ADD LEVEL 1 TO RESULT
# =========================================================
#
# if level:
#
# level = [9, 20]
#
# It is not empty.
#
#
# res.append(level)
#
# res = [
#     [3],
#     [9, 20]
# ]
#
#
# =========================================================
# STEP 7: THIRD WHILE LOOP — LEVEL 2
# =========================================================
#
# Queue currently contains:
#
# q = [None, None, 15, 7]
#
# Why are the None values there?
#
# Because node 9 had no children, so we added:
#
# q.append(None)
# q.append(None)
#
# These None values will simply be ignored by:
#
# if node:
#
#
# qLen = len(q)
#
# qLen = 4
#
# HOWEVER:
#
# Notice that only 15 and 7 are actual nodes.
#
# We process the four queue entries, but only add
# actual nodes to the current level.
#
# This implementation therefore works, but it carries
# None values in the queue.
#
#
# level = []
#
#
# =========================================================
# STEP 8: PROCESS LEVEL 2
# =========================================================
#
# First iteration:
#
# node = q.popleft()
#
# node = None
#
# if node:
#
# False
#
# Nothing is added.
#
#
# Second iteration:
#
# node = q.popleft()
#
# node = None
#
# if node:
#
# False
#
# Nothing is added.
#
#
# Third iteration:
#
# node = q.popleft()
#
# node = 15
#
# if node:
#     True
#
# level.append(15)
#
# level = [15]
#
# Node 15 has no children:
#
# q.append(None)
# q.append(None)
#
#
# Fourth iteration:
#
# node = q.popleft()
#
# node = 7
#
# if node:
#     True
#
# level.append(7)
#
# level = [15, 7]
#
# Node 7 has no children:
#
# q.append(None)
# q.append(None)
#
#
# =========================================================
# STEP 9: ADD LEVEL 2
# =========================================================
#
# level = [15, 7]
#
# Therefore:
#
# res.append(level)
#
# res = [
#     [3],
#     [9, 20],
#     [15, 7]
# ]
#
#
# =========================================================
# STEP 10: LOOP ENDS
# =========================================================
#
# Eventually all queue entries are processed.
#
# q becomes empty.
#
# Therefore:
#
# while q:
#
# becomes False.
#
# Exit the while loop.
#
#
# return res
#
# FINAL ANSWER:
#
# [[3], [9, 20], [15, 7]]
#
#
# =========================================================
# BIG PICTURE
# =========================================================
#
# LEVEL 0:
#
# q = [3]
# qLen = 1
# process → 3
# res = [[3]]
#
#
# LEVEL 1:
#
# q = [9, 20]
# qLen = 2
# process → 9, 20
# res = [[3], [9, 20]]
#
#
# LEVEL 2:
#
# q contains the children of 9 and 20.
# Actual nodes → 15, 7
#
# process → 15, 7
# res = [[3], [9, 20], [15, 7]]
#
#
# =========================================================
# MOST IMPORTANT PATTERN
# =========================================================
#
# while q:
#
#     qLen = len(q)      ← HOW MANY NODES IN THIS LEVEL?
#
#     level = []
#
#     for i in range(qLen):
#         node = q.popleft()
#
#         # process current node
#         # add its children to queue
#
#     res.append(level)
#
#
# qLen is the key.
#
# It tells us how many nodes belong to the CURRENT level.
#
# We process exactly those nodes.
#
# Their children are added to q and will be processed
# during the NEXT while-loop iteration.
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
# Every node is processed once.
#
# Space: O(n)
#
# The queue can contain up to O(n) nodes in the worst case.
#
# More precisely, auxiliary space is O(w), where w is
# the maximum width of the tree.
#
# =========================================================
        