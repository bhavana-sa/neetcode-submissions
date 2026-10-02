class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[l]  
# nums = [4, 5, 6, 7, 0, 1, 2]
#
# Index:
#        0  1  2  3  4  5  6
# nums = [4, 5, 6, 7, 0, 1, 2]
#
# Goal:
# Find the SMALLEST number.
#
# -----------------------------------
# INITIAL
#
# l = 0
# r = 6
#
# Search area:
#
# [4, 5, 6, 7, 0, 1, 2]
#  ↑                 ↑
#  l                 r
#
# -----------------------------------
# STEP 1
#
# m = l + (r - l) // 2
#   = 0 + (6 - 0) // 2
#   = 3
#
# nums[m] = nums[3] = 7
# nums[r] = nums[6] = 2
#
# Compare:
#
# nums[m] < nums[r]?
#
# 7 < 2 -> NO
#
# This tells us the minimum must be to the RIGHT
# of m.
#
# Why?
#
# We have:
#
# [4, 5, 6, 7 | 0, 1, 2]
#             ↑
#             m
#
# The rotation point / minimum is on the right.
#
# So:
#
# l = m + 1
#   = 4
#
# -----------------------------------
# STEP 2
#
# l = 4
# r = 6
#
# Search area:
#
# [0, 1, 2]
#  ↑     ↑
#  l     r
#
# m = 4 + (6 - 4) // 2
#   = 5
#
# nums[m] = nums[5] = 1
# nums[r] = nums[6] = 2
#
# Compare:
#
# 1 < 2 -> YES
#
# This tells us the minimum is at m
# OR somewhere to the LEFT of m.
#
# IMPORTANT:
# We CANNOT do r = m - 1
# because nums[m] itself could be the minimum.
#
# So:
#
# r = m
#   = 5
#
# -----------------------------------
# STEP 3
#
# l = 4
# r = 5
#
# Search area:
#
# [0, 1]
#  ↑  ↑
#  l  r
#
# m = 4 + (5 - 4) // 2
#   = 4
#
# nums[m] = 0
# nums[r] = 1
#
# Compare:
#
# 0 < 1 -> YES
#
# Therefore:
# minimum is at m OR to the left.
#
# r = m
#   = 4
#
# -----------------------------------
# NOW:
#
# l = 4
# r = 4
#
# while l < r
#
# 4 < 4 -> FALSE
#
# STOP.
#
# l points directly at the minimum.
#
# nums[l] = nums[4]
#       = 0
#
# return nums[l]
#
# return 0
#
# -----------------------------------
# FINAL ANSWER:
#
# 0
#
# -----------------------------------
# MOST IMPORTANT LOGIC:
#
# Compare nums[m] with nums[r].
#
# CASE 1:
#
# nums[m] < nums[r]
#
# Example:
#       1 < 2
#
# The right side is sorted:
#
# [0, 1, 2]
#
# The minimum could be m or somewhere LEFT.
#
# Therefore:
#     r = m
#
# -----------------------------------
# CASE 2:
#
# nums[m] >= nums[r]
#
# Example:
#       7 >= 2
#
# The minimum must be to the RIGHT of m.
#
# Therefore:
#     l = m + 1
#
# -----------------------------------
# WHY r = m AND NOT r = m - 1?
#
# Because nums[m] could itself be the minimum.
#
# Example:
#
# [0, 1, 2]
#  ↑
#  m
#
# If we removed m with:
# r = m - 1
#
# we'd accidentally throw away the answer.
#
# So we keep m:
#
# r = m
#
# -----------------------------------
# WHY l = m + 1?
#
# In the other case, we know nums[m] is NOT
# the minimum.
#
# Example:
#
# [4, 5, 6, 7, 0, 1, 2]
#          ↑
#          m
#
# Since 7 > 2, the minimum must be after m.
#
# Therefore we can safely discard m:
#
# l = m + 1
#
# -----------------------------------
# MENTAL MODEL:
#
# Compare MID with RIGHT.
#
# nums[m] < nums[r]
#     ↓
# minimum is LEFT or AT m
#     ↓
# r = m
#
# nums[m] >= nums[r]
#     ↓
# minimum is RIGHT of m
#     ↓
# l = m + 1
#
# Continue until:
#
# l == r
#
# That index is the minimum.
#
# -----------------------------------
# TIME: O(log n)
# SPACE: O(1)      