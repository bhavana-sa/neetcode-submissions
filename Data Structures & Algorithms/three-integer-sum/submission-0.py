class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, val in enumerate(nums):
            if val > 0:
                break
            if i > 0 and val == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = val + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([val, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l +=1
        return res
# nums = [-1, 0, 1, 2, -1, -4]
#
# Goal:
# Find all UNIQUE triplets whose sum is 0.
#
# -----------------------------------
# STEP 1: Sort the array
#
# nums.sort()
#
# nums = [-4, -1, -1, 0, 1, 2]
#
# res = []
#
# -----------------------------------
# i = 0
# a = nums[0] = -4
#
# Is a > 0?
# -4 > 0 -> NO
#
# Is this a duplicate of the previous a?
# i = 0, so NO.
#
# Set two pointers:
#
# l = i + 1 = 1
# r = len(nums) - 1 = 5
#
# Array:
#       a   l              r
#       ↓   ↓              ↓
#      -4  -1  -1   0   1   2
#
# -----------------------------------
# while l < r:
#
# l = 1, r = 5
#
# threeSum = -4 + (-1) + 2
#          = -3
#
# -3 < 0
#
# The sum is TOO SMALL.
# We need a BIGGER number.
#
# Move l right:
# l = 2
#
# -----------------------------------
# l = 2, r = 5
#
# threeSum = -4 + (-1) + 2
#          = -3
#
# Still too small.
#
# Move l:
# l = 3
#
# -----------------------------------
# l = 3, r = 5
#
# threeSum = -4 + 0 + 2
#          = -2
#
# Still too small.
#
# Move l:
# l = 4
#
# -----------------------------------
# l = 4, r = 5
#
# threeSum = -4 + 1 + 2
#          = -1
#
# Still too small.
#
# Move l:
# l = 5
#
# Now l == r.
#
# while l < r -> FALSE
#
# Done with a = -4.
#
# -----------------------------------
# i = 1
# a = nums[1] = -1
#
# Is a > 0?
# -1 > 0 -> NO
#
# Is it a duplicate?
# nums[1] == nums[0]?
# -1 == -4 -> NO
#
# Set pointers:
#
# l = 2
# r = 5
#
# Array:
#          a   l           r
#          ↓   ↓           ↓
#      -4  -1  -1   0   1   2
#
# -----------------------------------
# l = 2, r = 5
#
# threeSum = -1 + (-1) + 2
#          = 0
#
# FOUND A VALID TRIPLET!
#
# Add:
# res.append([-1, -1, 2])
#
# res = [[-1, -1, 2]]
#
# Move both pointers:
# l = 3
# r = 4
#
# -----------------------------------
# l = 3, r = 4
#
# threeSum = -1 + 0 + 1
#          = 0
#
# FOUND ANOTHER VALID TRIPLET!
#
# Add:
# res.append([-1, 0, 1])
#
# res = [[-1, -1, 2], [-1, 0, 1]]
#
# Move both:
# l = 4
# r = 3
#
# Now l < r -> FALSE
#
# Done with a = -1.
#
# -----------------------------------
# i = 2
# a = nums[2] = -1
#
# Check duplicate:
#
# i > 0 -> YES
# a == nums[i - 1]?
# -1 == nums[1]
# -1 == -1 -> YES
#
# This is a duplicate first number.
#
# continue
#
# Skip this iteration.
#
# -----------------------------------
# i = 3
# a = nums[3] = 0
#
# Is a > 0?
# 0 > 0 -> NO
#
# Is it a duplicate?
# 0 == -1 -> NO
#
# Set:
# l = 4
# r = 5
#
# -----------------------------------
# l = 4, r = 5
#
# threeSum = 0 + 1 + 2
#          = 3
#
# 3 > 0
#
# Sum is TOO LARGE.
# We need a SMALLER number.
#
# Move r left:
# r = 4
#
# Now l == r.
#
# while l < r -> FALSE
#
# Done with a = 0.
#
# -----------------------------------
# i = 4
# a = nums[4] = 1
#
# Is a > 0?
# 1 > 0 -> YES
#
# break
#
# Why can we stop?
#
# The array is sorted, so everything after 1
# is also positive.
#
# Positive + positive + positive
# can never equal 0.
#
# -----------------------------------
# return res
#
# res = [[-1, -1, 2], [-1, 0, 1]]
#
# FINAL ANSWER:
# [[-1, -1, 2], [-1, 0, 1]]
#
# -----------------------------------
# MAIN POINTER RULE TO REMEMBER:
#
# threeSum < 0
# -> sum is too small
# -> need a BIGGER number
# -> l += 1
#
# threeSum > 0
# -> sum is too large
# -> need a SMALLER number
# -> r -= 1
#
# threeSum == 0
# -> found answer
# -> save it
# -> move BOTH pointers
        