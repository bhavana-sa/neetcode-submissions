class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res
        # DRY RUN
#
# Input:
# nums = [1, 2, 3, 4]
#
# We need the product of every number EXCEPT nums[i].
#
# Expected output:
# [24, 12, 8, 6]
#
# --------------------------------------------------
# INITIALIZATION
# --------------------------------------------------
#
# res = [1] * len(nums)
#
# len(nums) = 4
#
# res = [1, 1, 1, 1]
#
# prefix = 1
#
# --------------------------------------------------
# FIRST LOOP: BUILD PREFIX PRODUCTS
# --------------------------------------------------
#
# for i in range(len(nums)):
#
# We go from LEFT to RIGHT.
#
# --------------------------------------------------
# i = 0
# --------------------------------------------------
#
# nums[0] = 1
# prefix = 1
#
# res[0] = prefix
# res[0] = 1
#
# res = [1, 1, 1, 1]
#
# Now update prefix:
#
# prefix *= nums[0]
# prefix = 1 * 1
# prefix = 1
#
# --------------------------------------------------
# i = 1
# --------------------------------------------------
#
# nums[1] = 2
# prefix = 1
#
# res[1] = prefix
# res[1] = 1
#
# res = [1, 1, 1, 1]
#
# Now update prefix:
#
# prefix *= nums[1]
# prefix = 1 * 2
# prefix = 2
#
# --------------------------------------------------
# i = 2
# --------------------------------------------------
#
# nums[2] = 3
# prefix = 2
#
# res[2] = prefix
# res[2] = 2
#
# res = [1, 1, 2, 1]
#
# Now update prefix:
#
# prefix *= nums[2]
# prefix = 2 * 3
# prefix = 6
#
# --------------------------------------------------
# i = 3
# --------------------------------------------------
#
# nums[3] = 4
# prefix = 6
#
# res[3] = prefix
# res[3] = 6
#
# res = [1, 1, 2, 6]
#
# Now update prefix:
#
# prefix *= nums[3]
# prefix = 6 * 4
# prefix = 24
#
# FIRST LOOP FINISHED
#
# res = [1, 1, 2, 6]
#
# What does res contain now?
#
# res[0] = product of numbers BEFORE index 0 = 1
# res[1] = product of numbers BEFORE index 1 = 1
# res[2] = product of numbers BEFORE index 2 = 1 * 2 = 2
# res[3] = product of numbers BEFORE index 3 = 1 * 2 * 3 = 6
#
# So:
#
# res = [1, 1, 2, 6]
#
# --------------------------------------------------
# SECOND LOOP: ADD SUFFIX PRODUCTS
# --------------------------------------------------
#
# suffix = 1
#
# We now go from RIGHT to LEFT.
#
# for i in range(len(nums) - 1, -1, -1):
#
# i will be:
# 3 → 2 → 1 → 0
#
# --------------------------------------------------
# i = 3
# --------------------------------------------------
#
# nums[3] = 4
# suffix = 1
#
# Current res[3] = 6
#
# res[3] *= suffix
#
# res[3] = 6 * 1
# res[3] = 6
#
# res = [1, 1, 2, 6]
#
# Now update suffix:
#
# suffix *= nums[3]
# suffix = 1 * 4
# suffix = 4
#
# --------------------------------------------------
# i = 2
# --------------------------------------------------
#
# nums[2] = 3
# suffix = 4
#
# Current res[2] = 2
#
# res[2] *= suffix
#
# res[2] = 2 * 4
# res[2] = 8
#
# res = [1, 1, 8, 6]
#
# Now update suffix:
#
# suffix *= nums[2]
# suffix = 4 * 3
# suffix = 12
#
# --------------------------------------------------
# i = 1
# --------------------------------------------------
#
# nums[1] = 2
# suffix = 12
#
# Current res[1] = 1
#
# res[1] *= suffix
#
# res[1] = 1 * 12
# res[1] = 12
#
# res = [1, 12, 8, 6]
#
# Now update suffix:
#
# suffix *= nums[1]
# suffix = 12 * 2
# suffix = 24
#
# --------------------------------------------------
# i = 0
# --------------------------------------------------
#
# nums[0] = 1
# suffix = 24
#
# Current res[0] = 1
#
# res[0] *= suffix
#
# res[0] = 1 * 24
# res[0] = 24
#
# res = [24, 12, 8, 6]
#
# Now update suffix:
#
# suffix *= nums[0]
# suffix = 24 * 1
# suffix = 24
#
# --------------------------------------------------
# FINAL ANSWER
# --------------------------------------------------
#
# return res
#
# return [24, 12, 8, 6]
#
# Why?
#
# For index 0:
# product except nums[0]
# = 2 * 3 * 4
# = 24
#
# For index 1:
# product except nums[1]
# = 1 * 3 * 4
# = 12
#
# For index 2:
# product except nums[2]
# = 1 * 2 * 4
# = 8
#
# For index 3:
# product except nums[3]
# = 1 * 2 * 3
# = 6
#
# FINAL OUTPUT:
# [24, 12, 8, 6]
        