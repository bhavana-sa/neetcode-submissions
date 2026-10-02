# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
# Example linked list:
#
# 1 → 2 → 3 → None
#
# head = 1
#
# Initially:
#
# prev = None
# curr = head = 1
#
# Visual:
#
# prev        curr
#  ↓           ↓
# None        1 → 2 → 3 → None
#
# -----------------------------------
# ITERATION 1
#
# curr = 1
#
# First:
#
# temp = curr.next
#
# temp = 1.next
#      = 2
#
# We save 2 because we're about to change
# curr.next.
#
# Visual:
#
# prev        curr       temp
#  ↓           ↓          ↓
# None        1  →       2 → 3 → None
#
# -----------------------------------
# Next:
#
# curr.next = prev
#
# 1.next = None
#
# We reverse the arrow:
#
# Before:
# 1 → 2
#
# After:
# 1 → None
#
# Visual:
#
# prev        curr       temp
#  ↓           ↓          ↓
# None        1           2 → 3 → None
#             ↓
#           None
#
# -----------------------------------
# Next:
#
# prev = curr
#
# prev = 1
#
# Visual:
#
#             curr
#              ↓
#              1
#              ↓
#            None
#
# prev
#  ↓
#  1
#
# -----------------------------------
# Next:
#
# curr = temp
#
# curr = 2
#
# Now:
#
# prev       curr
#  ↓          ↓
#  1          2 → 3 → None
#  ↓
# None
#
# -----------------------------------
# ITERATION 2
#
# curr = 2
#
# Save the next node:
#
# temp = curr.next
#      = 3
#
# Visual:
#
# prev       curr       temp
#  ↓          ↓          ↓
#  1          2          3 → None
#  ↓
# None
#
# -----------------------------------
# Reverse curr.next:
#
# curr.next = prev
#
# 2.next = 1
#
# Now:
#
# 2 → 1 → None
#
# Visual:
#
# prev       curr       temp
#  ↓          ↓          ↓
#  1 ←        2          3 → None
#  ↓
# None
#
# -----------------------------------
# Move prev:
#
# prev = curr
#
# prev = 2
#
# -----------------------------------
# Move curr:
#
# curr = temp
#
# curr = 3
#
# Now:
#
# prev       curr
#  ↓          ↓
#  2          3 → None
#  ↓          ↑
#  1
#  ↓
# None
#
# -----------------------------------
# ITERATION 3
#
# curr = 3
#
# Save next:
#
# temp = curr.next
#      = None
#
# -----------------------------------
# Reverse:
#
# curr.next = prev
#
# 3.next = 2
#
# Now:
#
# 3 → 2 → 1 → None
#
# -----------------------------------
# Move prev:
#
# prev = curr
#      = 3
#
# Move curr:
#
# curr = temp
#      = None
#
# Now:
#
# prev
#  ↓
#  3 → 2 → 1 → None
#
# curr
#  ↓
# None
#
# -----------------------------------
# while curr:
#
# curr = None
#
# None is False
#
# So the loop stops.
#
# -----------------------------------
# return prev
#
# prev is pointing to 3,
# which is now the first node.
#
# return 3
#
# FINAL LINKED LIST:
#
# 3 → 2 → 1 → None
#
# -----------------------------------
# THE 4 LINES TO UNDERSTAND:
#
# temp = curr.next
#
# Save the next node BEFORE changing the pointer.
#
# curr.next = prev
#
# Reverse the current node's arrow.
#
# prev = curr
#
# Move prev forward.
#
# curr = temp
#
# Move curr forward using the saved node.
#
# -----------------------------------
# EASY MEMORY TRICK:
#
# SAVE → REVERSE → MOVE PREV → MOVE CURR
#
# 1. Save next:
#       temp = curr.next
#
# 2. Reverse:
#       curr.next = prev
#
# 3. Move prev:
#       prev = curr
#
# 4. Move curr:
#       curr = temp
#
# -----------------------------------
# TIME: O(n)
# We visit every node once.
#
# SPACE: O(1)
# We only use prev, curr, and temp.
        