class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub, curSum = nums[0], 0
        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSub = max(maxSub, curSum)
        return maxSub
# Input:
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#
# We need to find the contiguous subarray
# with the largest sum.
#
# The best subarray is:
#
# [4, -1, 2, 1]
#
# Its sum is:
#
# 4 + (-1) + 2 + 1 = 6
#
# Expected answer = 6
#
# --------------------------------------------------
# INITIALIZATION
# --------------------------------------------------
#
# maxSub = nums[0]
# maxSub = -2
#
# curSum = 0
#
# maxSub = the largest subarray sum seen so far.
#
# curSum = the sum of the current subarray we are considering.
#
# --------------------------------------------------
# num = -2
# --------------------------------------------------
#
# curSum = 0
#
# Check:
#
# if curSum < 0
#
# 0 < 0 is False
#
# So curSum stays 0.
#
# Add current number:
#
# curSum += num
# curSum = 0 + (-2)
# curSum = -2
#
# Update maxSub:
#
# maxSub = max(-2, -2)
# maxSub = -2
#
# Current state:
# curSum = -2
# maxSub = -2
#
# --------------------------------------------------
# num = 1
# --------------------------------------------------
#
# curSum = -2
#
# Check:
#
# if curSum < 0
#
# -2 < 0 → True
#
# So:
#
# curSum = 0
#
# WHY?
#
# A negative sum hurts any future subarray.
# Starting fresh with the next number is better.
#
# Now add num:
#
# curSum += 1
# curSum = 0 + 1
# curSum = 1
#
# Update maxSub:
#
# maxSub = max(-2, 1)
# maxSub = 1
#
# Current state:
# curSum = 1
# maxSub = 1
#
# --------------------------------------------------
# num = -3
# --------------------------------------------------
#
# curSum = 1
#
# Check:
#
# 1 < 0 → False
#
# Keep current subarray.
#
# Add -3:
#
# curSum = 1 + (-3)
# curSum = -2
#
# Update maxSub:
#
# maxSub = max(1, -2)
# maxSub = 1
#
# Current state:
# curSum = -2
# maxSub = 1
#
# --------------------------------------------------
# num = 4
# --------------------------------------------------
#
# curSum = -2
#
# Check:
#
# -2 < 0 → True
#
# Reset:
#
# curSum = 0
#
# Now add 4:
#
# curSum = 0 + 4
# curSum = 4
#
# Update maxSub:
#
# maxSub = max(1, 4)
# maxSub = 4
#
# Current state:
# curSum = 4
# maxSub = 4
#
# --------------------------------------------------
# num = -1
# --------------------------------------------------
#
# curSum = 4
#
# 4 < 0 → False
#
# Keep the current subarray.
#
# Add -1:
#
# curSum = 4 + (-1)
# curSum = 3
#
# Update maxSub:
#
# maxSub = max(4, 3)
# maxSub = 4
#
# Current state:
# curSum = 3
# maxSub = 4
#
# --------------------------------------------------
# num = 2
# --------------------------------------------------
#
# curSum = 3
#
# 3 < 0 → False
#
# Keep the current subarray.
#
# Add 2:
#
# curSum = 3 + 2
# curSum = 5
#
# Update maxSub:
#
# maxSub = max(4, 5)
# maxSub = 5
#
# Current state:
# curSum = 5
# maxSub = 5
#
# --------------------------------------------------
# num = 1
# --------------------------------------------------
#
# curSum = 5
#
# 5 < 0 → False
#
# Keep the current subarray.
#
# Add 1:
#
# curSum = 5 + 1
# curSum = 6
#
# Update maxSub:
#
# maxSub = max(5, 6)
# maxSub = 6
#
# Current state:
# curSum = 6
# maxSub = 6
#
# We have found:
#
# [4, -1, 2, 1]
#
# Sum = 6
#
# --------------------------------------------------
# num = -5
# --------------------------------------------------
#
# curSum = 6
#
# 6 < 0 → False
#
# Keep the current subarray.
#
# Add -5:
#
# curSum = 6 + (-5)
# curSum = 1
#
# Update maxSub:
#
# maxSub = max(6, 1)
# maxSub = 6
#
# Current state:
# curSum = 1
# maxSub = 6
#
# --------------------------------------------------
# num = 4
# --------------------------------------------------
#
# curSum = 1
#
# 1 < 0 → False
#
# Keep the current subarray.
#
# Add 4:
#
# curSum = 1 + 4
# curSum = 5
#
# Update maxSub:
#
# maxSub = max(6, 5)
# maxSub = 6
#
# Current state:
# curSum = 5
# maxSub = 6
#
# --------------------------------------------------
# LOOP FINISHED
# --------------------------------------------------
#
# maxSub = 6
#
# return maxSub
#
# FINAL ANSWER = 6
#
# The subarray that produced 6 was:
#
# [4, -1, 2, 1]
#
# 4 + (-1) + 2 + 1 = 6
#
# --------------------------------------------------
# KEY IDEA
# --------------------------------------------------
#
# curSum = sum of the current subarray.
#
# If curSum becomes negative:
#
#     curSum = 0
#
# because carrying a negative sum forward can only
# make a future subarray smaller.
#
# Then we start fresh from the next number.
#
# maxSub keeps track of the largest sum we've seen.
#
# So:
#
# curSum → current best subarray ending here
# maxSub → best subarray found anywhere so far
#
# TIME: O(n)
# We visit every number once.
#
# SPACE: O(1)
# We only use curSum and maxSub.
        