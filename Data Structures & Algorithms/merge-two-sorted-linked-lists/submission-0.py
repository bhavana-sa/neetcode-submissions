# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        node.next = list1 or list2
        return temp.next
# list1 = 1 → 2 → 4 → None
# list2 = 1 → 3 → 4 → None
#
# -----------------------------------
# INITIALIZATION
#
# dummy = node = ListNode()
#
# We create an empty dummy node.
#
# dummy
#   ↓
# [0] → None
#
# node also points to this dummy node.
#
# dummy ──→ [0]
# node  ──→ [0]
#
# Why dummy?
# It gives us an easy starting point so we don't
# have to handle the first node as a special case.
#
# -----------------------------------
# ITERATION 1
#
# list1.val = 1
# list2.val = 1
#
# Compare:
#
# list1.val < list2.val
# 1 < 1 -> NO
#
# So choose list2.
#
# node.next = list2
#
# Now:
#
# dummy → [0] → 1
#                  ↑
#                list2
#
# Move list2:
#
# list2 = list2.next
#
# list2 now points to 3.
#
# Move node:
#
# node = node.next
#
# node now points to the 1 we just added.
#
# -----------------------------------
# CURRENT:
#
# dummy
#   ↓
# [0] → 1
#       ↑
#      node
#
# list1:
# 1 → 2 → 4
#
# list2:
# 3 → 4
#
# -----------------------------------
# ITERATION 2
#
# list1.val = 1
# list2.val = 3
#
# Compare:
#
# 1 < 3 -> YES
#
# Choose list1.
#
# node.next = list1
#
# The 1 from list1 is attached.
#
# Move list1:
#
# list1 = list1.next
#
# list1 now points to 2.
#
# Move node:
#
# node = node.next
#
# -----------------------------------
# CURRENT:
#
# dummy
#   ↓
# [0] → 1 → 1
#            ↑
#           node
#
# list1:
# 2 → 4
#
# list2:
# 3 → 4
#
# -----------------------------------
# ITERATION 3
#
# list1.val = 2
# list2.val = 3
#
# 2 < 3 -> YES
#
# Choose list1.
#
# node.next = list1
#
# Move list1:
# list1 = list1.next
#
# list1 now points to 4.
#
# Move node:
# node = node.next
#
# -----------------------------------
# CURRENT:
#
# dummy
#   ↓
# [0] → 1 → 1 → 2
#                ↑
#               node
#
# list1:
# 4
#
# list2:
# 3 → 4
#
# -----------------------------------
# ITERATION 4
#
# list1.val = 4
# list2.val = 3
#
# 4 < 3 -> NO
#
# Choose list2.
#
# node.next = list2
#
# Move list2:
# list2 = list2.next
#
# list2 now points to 4.
#
# Move node:
# node = node.next
#
# -----------------------------------
# CURRENT:
#
# dummy
#   ↓
# [0] → 1 → 1 → 2 → 3
#                     ↑
#                    node
#
# list1:
# 4
#
# list2:
# 4
#
# -----------------------------------
# ITERATION 5
#
# list1.val = 4
# list2.val = 4
#
# 4 < 4 -> NO
#
# Choose list2.
#
# node.next = list2
#
# Move list2:
# list2 = list2.next
#
# list2 = None
#
# Move node:
# node = node.next
#
# -----------------------------------
# CURRENT:
#
# dummy
#   ↓
# [0] → 1 → 1 → 2 → 3 → 4
#                          ↑
#                         node
#
# list1:
# 4 → None
#
# list2:
# None
#
# -----------------------------------
# WHILE LOOP STOPS
#
# while list1 and list2:
#
# list2 is None
#
# So the loop ends.
#
# But list1 still has:
#
# 4 → None
#
# We need to attach the remaining nodes.
#
# -----------------------------------
# node.next = list1 or list2
#
# list1 exists, so:
#
# node.next = list1
#
# Attach the remaining 4:
#
# dummy
#   ↓
# [0] → 1 → 1 → 2 → 3 → 4 → 4 → None
#
# -----------------------------------
# return dummy.next
#
# dummy itself was just the fake starting node.
# We DON'T return dummy.
#
# dummy.next points to the REAL first node.
#
# return:
#
# 1 → 1 → 2 → 3 → 4 → 4 → None
#
# FINAL ANSWER:
#
# 1 → 1 → 2 → 3 → 4 → 4
#
# -----------------------------------
# IMPORTANT MENTAL MODEL:
#
# Compare:
#     list1.val vs list2.val
#
# Pick the SMALLER node.
#     ↓
# Attach it to node.next.
#     ↓
# Move that list forward.
#     ↓
# Move node forward.
#
# Repeat until one list is empty.
#
# Then attach whatever is left.
#
# -----------------------------------
# THE 3 POINTERS:
#
# dummy = remembers where the result starts
#
# node = builds the merged list
#
# list1/list2 = move through the input lists
#
# -----------------------------------
# IMPORTANT:
#
# dummy = node = ListNode()
#
# At the beginning, BOTH variables point to
# the SAME dummy node.
#
# Later:
#
# node moves forward,
# but dummy stays at the beginning.
#
# That's why we can eventually do:
#
# return dummy.next
#
# -----------------------------------
# TIME: O(n + m)
#
# We visit every node in both lists once.
#
# SPACE: O(1)
#
# We reuse the existing nodes instead of creating
# a new list of nodes.
        