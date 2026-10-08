class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l , total = 0, 0
        res = float("inf")
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1
        return 0 if res == float("inf") else res 
        # DRY RUN
#
# target = 10
# nums = [2, 1, 5, 1, 5, 3]
#
# Initial:
# l = 0
# total = 0
# res = infinity
#
# -----------------------------------
# STEP 1: r = 0, nums[r] = 2
#
# total = 0 + 2 = 2
# total >= 10? NO
#
# Window: [2]
# res = infinity
#
# -----------------------------------
# STEP 2: r = 1, nums[r] = 1
#
# total = 2 + 1 = 3
# total >= 10? NO
#
# Window: [2, 1]
# res = infinity
#
# -----------------------------------
# STEP 3: r = 2, nums[r] = 5
#
# total = 3 + 5 = 8
# total >= 10? NO
#
# Window: [2, 1, 5]
# res = infinity
#
# -----------------------------------
# STEP 4: r = 3, nums[r] = 1
#
# total = 8 + 1 = 9
# total >= 10? NO
#
# Window: [2, 1, 5, 1]
# res = infinity
#
# -----------------------------------
# STEP 5: r = 4, nums[r] = 5
#
# total = 9 + 5 = 14
# total >= 10? YES
#
# Window: [2, 1, 5, 1, 5]
# Length = 4 - 0 + 1 = 5
#
# res = min(infinity, 5) = 5
#
# Shrink from left:
#
# Remove nums[0] = 2
# total = 14 - 2 = 12
# l = 1
#
# total >= 10? YES
#
# Window: [1, 5, 1, 5]
# Length = 4 - 1 + 1 = 4
#
# res = min(5, 4) = 4
#
# Shrink again:
#
# Remove nums[1] = 1
# total = 12 - 1 = 11
# l = 2
#
# total >= 10? YES
#
# Window: [5, 1, 5]
# Length = 4 - 2 + 1 = 3
#
# res = min(4, 3) = 3
#
# Shrink again:
#
# Remove nums[2] = 5
# total = 11 - 5 = 6
# l = 3
#
# total >= 10? NO
# Stop shrinking.
#
# -----------------------------------
# STEP 6: r = 5, nums[r] = 3
#
# total = 6 + 3 = 9
# total >= 10? NO
#
# Window: [1, 5, 3]
# total = 9
# res = 3
#
# -----------------------------------
# END
#
# return res
#
# FINAL ANSWER = 3
#
# Shortest valid subarray:
# [5, 1, 5]
#
# Sum = 5 + 1 + 5 = 11
# Length = 3

        