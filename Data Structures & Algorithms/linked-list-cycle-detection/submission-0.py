# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
#
#       ┌──────────────┐
#       ↓              │
# 1 → 2 → 3 → 4 ───────┘
#
# The node 4 points back to node 2.
#
# So the list contains a cycle:
#
# 2 → 3 → 4 → 2 → 3 → 4 → ...
#
# -----------------------------------
# INITIAL
#
# slow = head
#      = node 1
#
# fast = head
#      = node 1
#
# Visual:
#
# slow
#  ↓
#  1 → 2 → 3 → 4
#  ↑           ↓
#  └───────────┘
# fast
#  ↑
#  1
#
# -----------------------------------
# ITERATION 1
#
# Check:
#
# while fast and fast.next
#
# fast = node 1 -> YES
# fast.next = node 2 -> YES
#
# Continue.
#
# Move slow ONE step:
#
# slow = slow.next
#
# slow = node 2
#
# Move fast TWO steps:
#
# fast = fast.next.next
#
# fast:
# node 1 → node 2 → node 3
#
# fast = node 3
#
# Now:
#
# slow = 2
# fast = 3
#
# Are they the same node?
# NO
#
# Continue.
#
# -----------------------------------
# ITERATION 2
#
# slow = node 2
# fast = node 3
#
# Move slow ONE step:
#
# slow = node 3
#
# Move fast TWO steps:
#
# node 3 → node 4 → node 2
#
# fast = node 2
#
# Now:
#
# slow = 3
# fast = 2
#
# slow == fast?
# NO
#
# Continue.
#
# -----------------------------------
# ITERATION 3
#
# slow = node 3
# fast = node 2
#
# Move slow ONE step:
#
# slow = node 4
#
# Move fast TWO steps:
#
# node 2 → node 3 → node 4
#
# fast = node 4
#
# Now:
#
# slow = 4
# fast = 4
#
# slow == fast?
# YES!
#
# return True
#
# -----------------------------------
# FINAL ANSWER:
#
# True
#
# The two pointers met inside the cycle.
#
# -----------------------------------
# WHY DOES THIS WORK?
#
# slow moves:
#
# 1 → 2 → 3 → 4 → 2 → 3 → 4 ...
#     +1   +1   +1
#
# fast moves:
#
# 1 → 3 → 2 → 4 → 3 → 2 → ...
#     +2   +2   +2
#
# If there is a cycle, fast keeps moving around
# the cycle and eventually catches slow.
#
# Think of two runners on a circular track:
#
# Slow runner = 1 step at a time
# Fast runner = 2 steps at a time
#
# On a circular track, the fast runner MUST
# eventually catch the slow runner.
#
# -----------------------------------
# WHAT IF THERE IS NO CYCLE?
#
# Example:
#
# 1 → 2 → 3 → 4 → None
#
# Eventually:
#
# fast = None
#
# or:
#
# fast.next = None
#
# Then:
#
# while fast and fast.next
#
# becomes FALSE.
#
# We exit the loop and:
#
# return False
#
# -----------------------------------
# IMPORTANT CONDITION:
#
# while fast and fast.next:
#
# We need BOTH to exist before doing:
#
# fast = fast.next.next
#
# Otherwise we could try to access
# .next on None.
#
# -----------------------------------
# IMPORTANT:
#
# slow == fast
#
# We are comparing NODE REFERENCES,
# not just their values.
#
# If two nodes happen to have the same value,
# that does NOT mean they are the same node.
#
# -----------------------------------
# MENTAL MODEL:
#
# slow → 1 step
# fast → 2 steps
#
# Cycle:
#     eventually meet
#     → True
#
# No cycle:
#     fast reaches None
#     → False
#
# -----------------------------------
# TIME: O(n)
#
# In the worst case, the pointers travel through
# the list/cycle a linear number of times.
#
# SPACE: O(1)
#
# We only use two pointers.

        