class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res
# Example:
# heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
#
# l = 0
# r = 8
# res = 0
#
# The area between two lines is:
#
# area = shorter height * width
#
# -----------------------------------
# STEP 1
#
# l = 0 -> heights[l] = 1
# r = 8 -> heights[r] = 7
#
# width = r - l
#       = 8 - 0
#       = 8
#
# height = min(1, 7)
#        = 1
#
# area = 1 * 8
#      = 8
#
# res = max(0, 8)
#     = 8
#
# Compare heights:
# 1 <= 7 -> YES
#
# Move l:
# l = 1
#
# -----------------------------------
# STEP 2
#
# l = 1 -> heights[l] = 8
# r = 8 -> heights[r] = 7
#
# width = 8 - 1 = 7
#
# height = min(8, 7)
#        = 7
#
# area = 7 * 7
#      = 49
#
# res = max(8, 49)
#     = 49
#
# Compare:
# 8 <= 7 -> NO
#
# Move r:
# r = 7
#
# -----------------------------------
# STEP 3
#
# l = 1 -> height = 8
# r = 7 -> height = 3
#
# width = 7 - 1 = 6
#
# height = min(8, 3)
#        = 3
#
# area = 3 * 6
#      = 18
#
# res = max(49, 18)
#     = 49
#
# Compare:
# 8 <= 3 -> NO
#
# Move r:
# r = 6
#
# -----------------------------------
# STEP 4
#
# l = 1 -> height = 8
# r = 6 -> height = 8
#
# width = 6 - 1 = 5
#
# height = min(8, 8)
#        = 8
#
# area = 8 * 5
#      = 40
#
# res = max(49, 40)
#     = 49
#
# Compare:
# 8 <= 8 -> YES
#
# Move l:
# l = 2
#
# -----------------------------------
# STEP 5
#
# l = 2 -> height = 6
# r = 6 -> height = 8
#
# width = 6 - 2 = 4
#
# height = min(6, 8)
#        = 6
#
# area = 6 * 4
#      = 24
#
# res = max(49, 24)
#     = 49
#
# Compare:
# 6 <= 8 -> YES
#
# Move l:
# l = 3
#
# -----------------------------------
# STEP 6
#
# l = 3 -> height = 2
# r = 6 -> height = 8
#
# width = 6 - 3 = 3
#
# height = min(2, 8)
#        = 2
#
# area = 2 * 3
#      = 6
#
# res = max(49, 6)
#     = 49
#
# Compare:
# 2 <= 8 -> YES
#
# Move l:
# l = 4
#
# -----------------------------------
# STEP 7
#
# l = 4 -> height = 5
# r = 6 -> height = 8
#
# width = 6 - 4 = 2
#
# height = min(5, 8)
#        = 5
#
# area = 5 * 2
#      = 10
#
# res = max(49, 10)
#     = 49
#
# Compare:
# 5 <= 8 -> YES
#
# Move l:
# l = 5
#
# -----------------------------------
# STEP 8
#
# l = 5 -> height = 4
# r = 6 -> height = 8
#
# width = 6 - 5 = 1
#
# height = min(4, 8)
#        = 4
#
# area = 4 * 1
#      = 4
#
# res = max(49, 4)
#     = 49
#
# Compare:
# 4 <= 8 -> YES
#
# Move l:
# l = 6
#
# Now l == r.
#
# while l < r -> FALSE
#
# -----------------------------------
# return res
#
# FINAL ANSWER = 49
#
# The maximum container is formed by:
# heights[1] = 8
# heights[8] = 7
#
# Width = 8 - 1 = 7
# Height = min(8, 7) = 7
#
# Area = 7 * 7 = 49
#
# -----------------------------------
# IMPORTANT POINTER LOGIC:
#
# The container is limited by the SHORTER line.
#
# If left is shorter:
#     heights[l] <= heights[r]
#     -> move l
#
# If right is shorter:
#     heights[r] < heights[l]
#     -> move r
#
# Why?
# Because moving the taller line cannot make the
# limiting height taller, while the width gets smaller.
#
# So we always move the SHORTER side,
# hoping to find a taller line.
#
# Mental model:
#
# SHORTER SIDE -> MOVE IT
# TALLER SIDE  -> KEEP IT

        