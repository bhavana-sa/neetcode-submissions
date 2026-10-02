class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1      
# Example:
# nums = [4, 5, 6, 7, 0, 1, 2]
# target = 0
#
# Index:
#          0  1  2  3  4  5  6
# nums =  [4, 5, 6, 7, 0, 1, 2]
#
# -----------------------------------
# INITIAL:
#
# l = 0
# r = 6
#
# -----------------------------------
# STEP 1
#
# mid = (l + r) // 2
#     = (0 + 6) // 2
#     = 3
#
# nums[mid] = nums[3] = 7
#
# Is target == nums[mid]?
#
# 0 == 7 -> NO
#
# -----------------------------------
# Now we need to figure out
# which HALF is sorted.
#
# Check:
#
# nums[l] <= nums[mid]
# 4 <= 7 -> YES
#
# Therefore:
# LEFT HALF is sorted.
#
# Sorted half:
#
# [4, 5, 6, 7]
#  ↑        ↑
#  l       mid
#
# Now ask:
# Is target 0 inside this sorted range [4, 7]?
#
# target > nums[mid]?
# 0 > 7 -> NO
#
# target < nums[l]?
# 0 < 4 -> YES
#
# Therefore target is NOT in the sorted left half.
#
# So search the RIGHT half.
#
# l = mid + 1
#   = 4
#
# -----------------------------------
# STEP 2
#
# l = 4
# r = 6
#
# Current search area:
#
# [0, 1, 2]
#  ↑     ↑
#  l     r
#
# mid = (4 + 6) // 2
#     = 5
#
# nums[mid] = nums[5] = 1
#
# Is target == nums[mid]?
#
# 0 == 1 -> NO
#
# -----------------------------------
# Determine which half is sorted.
#
# nums[l] <= nums[mid]
#
# nums[4] <= nums[5]
# 0 <= 1 -> YES
#
# LEFT HALF is sorted.
#
# Sorted half:
#
# [0, 1]
#  ↑  ↑
#  l mid
#
# Is target inside [0, 1]?
#
# target > nums[mid]?
# 0 > 1 -> NO
#
# target < nums[l]?
# 0 < 0 -> NO
#
# Therefore target IS inside this sorted half.
#
# Search left.
#
# r = mid - 1
#   = 4
#
# -----------------------------------
# STEP 3
#
# l = 4
# r = 4
#
# mid = (4 + 4) // 2
#     = 4
#
# nums[mid] = nums[4] = 0
#
# target == nums[mid]?
#
# 0 == 0 -> YES!
#
# return mid
#
# return 4
#
# -----------------------------------
# FINAL ANSWER:
#
# 4
#
# target 0 is at index 4.
#
# -----------------------------------
# IMPORTANT IDEA:
#
# Even though the whole array is rotated,
# at least ONE of the two halves around mid
# will always be sorted.
#
# Check:
#
# nums[l] <= nums[mid]
#
#       YES
#        ↓
# LEFT half is sorted
#
#       NO
#        ↓
# RIGHT half is sorted
#
# -----------------------------------
# IF LEFT HALF IS SORTED:
#
# nums[l] <= nums[mid]
#
# Ask:
# Is target INSIDE the sorted range?
#
# nums[l] <= target <= nums[mid]
#
# If YES:
#     r = mid - 1
#
# If NO:
#     l = mid + 1
#
# -----------------------------------
# IF RIGHT HALF IS SORTED:
#
# nums[l] > nums[mid]
#
# Ask:
# Is target INSIDE the sorted range?
#
# nums[mid] <= target <= nums[r]
#
# If YES:
#     l = mid + 1
#
# If NO:
#     r = mid - 1
#
# -----------------------------------
# EASY MENTAL MODEL:
#
# 1. Find mid.
# 2. Is target == nums[mid]?
#       YES -> return mid
#
# 3. Which half is sorted?
#
# 4. Is target inside that sorted half?
#
#       YES -> search that half
#       NO  -> search the other half
#
# 5. Repeat.
#
# -----------------------------------
# TIME:
# O(log n)
#
# SPACE:
# O(1)