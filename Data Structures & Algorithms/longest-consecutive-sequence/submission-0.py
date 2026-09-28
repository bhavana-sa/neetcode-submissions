class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num -1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length , longest)
        return longest
# DRY RUN
# Example:
# prices = [7, 1, 5, 3, 6, 4]
#
# Goal: Buy first, then sell later.
# We want the maximum profit possible.
#
# maxP = 0
# minBuy = prices[0] = 7
#
# -----------------------------------
# sell = 7
# profit = sell - minBuy
#        = 7 - 7
#        = 0
#
# maxP = max(0, 0) = 0
# minBuy = min(7, 7) = 7
#
# State:
# minBuy = 7
# maxP = 0
#
# -----------------------------------
# sell = 1
# profit = 1 - 7 = -6
#
# maxP = max(0, -6) = 0
# minBuy = min(7, 1) = 1
#
# We found a cheaper buying price, so update minBuy to 1.
#
# State:
# minBuy = 1
# maxP = 0
#
# -----------------------------------
# sell = 5
# profit = 5 - 1 = 4
#
# maxP = max(0, 4) = 4
# minBuy = min(1, 5) = 1
#
# Best profit so far = 4
#
# State:
# minBuy = 1
# maxP = 4
#
# -----------------------------------
# sell = 3
# profit = 3 - 1 = 2
#
# maxP = max(4, 2) = 4
# minBuy = min(1, 3) = 1
#
# 4 is still the best profit.
#
# State:
# minBuy = 1
# maxP = 4
#
# -----------------------------------
# sell = 6
# profit = 6 - 1 = 5
#
# maxP = max(4, 5) = 5
# minBuy = min(1, 6) = 1
#
# New best profit = 5
#
# State:
# minBuy = 1
# maxP = 5
#
# -----------------------------------
# sell = 4
# profit = 4 - 1 = 3
#
# maxP = max(5, 3) = 5
# minBuy = min(1, 4) = 1
#
# Best profit is still 5.
#
# -----------------------------------
# return maxP
# return 5
#
# Best transaction:
# Buy at 1
# Sell at 6
# Profit = 6 - 1 = 5
        