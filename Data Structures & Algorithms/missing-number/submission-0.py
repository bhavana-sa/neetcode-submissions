class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range (len(nums)):
            res += i - nums[i]
        return res        
# DRY RUN
#
# Input:
# nums = [3, 0, 1]
#
# The array has 3 elements.
#
# Therefore:
# n = len(nums) = 3
#
# The numbers should contain:
# 0, 1, 2, 3
#
# Actual numbers:
# 3, 0, 1
#
# Missing number = 2
#
# --------------------------------------------------
# INITIALIZATION
# --------------------------------------------------
#
# res = len(nums)
#
# len(nums) = 3
#
# Therefore:
# res = 3
#
# Current state:
# res = 3
#
# --------------------------------------------------
# LOOP
# --------------------------------------------------
#
# for i in range(len(nums)):
#
# len(nums) = 3
#
# range(3) gives:
#
# i = 0
# i = 1
# i = 2
#
# --------------------------------------------------
# ITERATION 1: i = 0
# --------------------------------------------------
#
# Current array:
#
# index:  0   1   2
# value:  3   0   1
#         ↑
#       nums[0]
#
# nums[0] = 3
#
# Execute:
#
# res += i - nums[i]
#
# Substitute the values:
#
# res += 0 - nums[0]
#
# res += 0 - 3
#
# res += -3
#
# res was 3:
#
# res = 3 + (-3)
#     = 0
#
# Current state:
# res = 0
#
# --------------------------------------------------
# ITERATION 2: i = 1
# --------------------------------------------------
#
# Current array:
#
# index:  0   1   2
# value:  3   0   1
#             ↑
#           nums[1]
#
# nums[1] = 0
#
# Execute:
#
# res += i - nums[i]
#
# Substitute the values:
#
# res += 1 - nums[1]
#
# res += 1 - 0
#
# res += 1
#
# res was 0:
#
# res = 0 + 1
#     = 1
#
# Current state:
# res = 1
#
# --------------------------------------------------
# ITERATION 3: i = 2
# --------------------------------------------------
#
# Current array:
#
# index:  0   1   2
# value:  3   0   1
#                 ↑
#               nums[2]
#
# nums[2] = 1
#
# Execute:
#
# res += i - nums[i]
#
# Substitute the values:
#
# res += 2 - nums[2]
#
# res += 2 - 1
#
# res += 1
#
# res was 1:
#
# res = 1 + 1
#     = 2
#
# Current state:
# res = 2
#
# --------------------------------------------------
# LOOP FINISHED
# --------------------------------------------------
#
# All indices 0, 1, 2 have been processed.
#
# Current:
# res = 2
#
# Execute:
#
# return res
#
# return 2
#
# FINAL ANSWER = 2