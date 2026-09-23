class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n -1
            res += 1
        return res
# DRY RUN
#
# Input:
# n = 11
#
# Binary representation:
# 11 = 1011
#
# We need to count how many 1s are in 1011.
#
# 1011 has three 1s, so we expect the answer to be 3.
#
# --------------------------------------------------
# INITIAL STATE
# --------------------------------------------------
#
# n = 1011
# res = 0
#
# n is not 0, so enter the while loop.
#
# --------------------------------------------------
# FIRST ITERATION
# --------------------------------------------------
#
# Current:
# n = 1011
# res = 0
#
# Execute:
# n &= n - 1
#
# First calculate n - 1:
#
#     1011
#   -    1
#   ------
#     1010
#
# So:
# n - 1 = 1010
#
# Now perform AND:
#
#     1011
#   & 1010
#   ------
#     1010
#
# Therefore:
# n = 1010
#
# The rightmost 1 was removed.
#
# Then:
# res += 1
#
# res = 1
#
# Current state:
# n = 1010
# res = 1
#
# --------------------------------------------------
# SECOND ITERATION
# --------------------------------------------------
#
# n is still not 0, so continue.
#
# Current:
# n = 1010
# res = 1
#
# Execute:
# n &= n - 1
#
# First:
#
#     1010
#   -    1
#   ------
#     1001
#
# So:
# n - 1 = 1001
#
# Now AND:
#
#     1010
#   & 1001
#   ------
#     1000
#
# Therefore:
# n = 1000
#
# One more 1 was removed.
#
# Then:
# res += 1
#
# res = 2
#
# Current state:
# n = 1000
# res = 2
#
# --------------------------------------------------
# THIRD ITERATION
# --------------------------------------------------
#
# n is still not 0, so continue.
#
# Current:
# n = 1000
# res = 2
#
# Execute:
# n &= n - 1
#
# First:
#
#     1000
#   -    1
#   ------
#     0111
#
# So:
# n - 1 = 0111
#
# Now AND:
#
#     1000
#   & 0111
#   ------
#     0000
#
# Therefore:
# n = 0000
#
# The last 1 was removed.
#
# Then:
# res += 1
#
# res = 3
#
# Current state:
# n = 0000
# res = 3
#
# --------------------------------------------------
# LOOP ENDS
# --------------------------------------------------
#
# while n:
#
# n is now 0, so the loop stops.
#
# return res
#
# return 3
#
# FINAL ANSWER = 3

        