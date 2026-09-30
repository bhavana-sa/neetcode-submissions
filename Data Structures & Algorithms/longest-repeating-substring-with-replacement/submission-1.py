class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        maxf = 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
# s = "AABABBA"
# k = 1
#
# We can change AT MOST 1 character.
#
# Goal:
# Find the longest substring that can become
# the same character after at most k replacements.
#
# -----------------------------------
# IMPORTANT IDEA
#
# For every window:
#
# window length = r - l + 1
#
# maxf = frequency of the MOST COMMON character
#
# Characters we need to replace:
#
# window length - maxf
#
# If this number <= k:
#     window is VALID
#
# If this number > k:
#     window is INVALID
#     -> shrink from the left
#
# -----------------------------------
#
# INITIAL:
#
# count = {}
# res = 0
# l = 0
# maxf = 0
#
# -----------------------------------
# r = 0
# s[r] = 'A'
#
# count['A'] = 1
#
# count = {'A': 1}
#
# maxf = max(0, 1)
#      = 1
#
# Window:
# [A]
#
# window length = 0 - 0 + 1
#               = 1
#
# replacements needed:
# 1 - 1 = 0
#
# 0 <= k(1)
# VALID
#
# res = max(0, 1)
#     = 1
#
# -----------------------------------
# r = 1
# s[r] = 'A'
#
# count['A'] = 2
#
# count = {'A': 2}
#
# maxf = max(1, 2)
#      = 2
#
# Window:
# [A A]
#
# length = 2
#
# replacements needed:
# 2 - 2 = 0
#
# VALID
#
# res = max(1, 2)
#     = 2
#
# -----------------------------------
# r = 2
# s[r] = 'B'
#
# count['B'] = 1
#
# count = {'A': 2, 'B': 1}
#
# maxf = max(2, 1)
#      = 2
#
# Window:
# [A A B]
#
# length = 3
#
# Most common character = A
# maxf = 2
#
# We need to replace:
# B -> A
#
# replacements needed:
# 3 - 2 = 1
#
# 1 <= k(1)
# VALID
#
# res = max(2, 3)
#     = 3
#
# Window "AAB" can become "AAA"
# with 1 replacement.
#
# -----------------------------------
# r = 3
# s[r] = 'A'
#
# count['A'] = 3
#
# count = {'A': 3, 'B': 1}
#
# maxf = 3
#
# Window:
# [A A B A]
#
# length = 4
#
# Most common = A
# maxf = 3
#
# replacements needed:
# 4 - 3 = 1
#
# 1 <= k
# VALID
#
# res = max(3, 4)
#     = 4
#
# Window "AABA"
# can become "AAAA"
# by replacing B with A.
#
# -----------------------------------
# r = 4
# s[r] = 'B'
#
# count['B'] = 2
#
# count = {'A': 3, 'B': 2}
#
# maxf = max(3, 2)
#      = 3
#
# Window:
# [A A B A B]
#
# length = 5
#
# replacements needed:
# 5 - 3 = 2
#
# 2 > k(1)
#
# WINDOW IS INVALID.
#
# We need to shrink from the LEFT.
#
# -----------------------------------
# while condition:
#
# (r - l + 1) - maxf > k
#
# = 5 - 3
# = 2
#
# 2 > 1 -> TRUE
#
# Remove s[l]:
#
# s[0] = 'A'
#
# count['A'] -= 1
#
# count = {'A': 2, 'B': 2}
#
# l = 1
#
# -----------------------------------
# Check while condition again:
#
# Window is now:
# [A B A B]
#
# length = 4
#
# maxf is still 3 in this code.
#
# replacements needed according to stored maxf:
# 4 - 3 = 1
#
# 1 <= k
#
# Stop shrinking.
#
# res = max(4, 4)
#     = 4
#
# IMPORTANT:
# maxf is NOT decreased here.
# That's intentional in this standard solution.
#
# We only need maxf as the highest frequency
# we've seen while expanding the window.
#
# -----------------------------------
# r = 5
# s[r] = 'B'
#
# count['B'] = 3
#
# count = {'A': 2, 'B': 3}
#
# maxf = max(3, 3)
#      = 3
#
# Current window:
# [A B A B B]
#
# length = 5
#
# replacements needed:
# 5 - 3 = 2
#
# 2 > k(1)
#
# INVALID.
#
# Shrink from left.
#
# Remove s[l]:
# s[1] = 'A'
#
# count['A'] = 1
#
# l = 2
#
# -----------------------------------
# Check again:
#
# Current window:
# [B A B B]
#
# length = 4
#
# 4 - maxf(3)
# = 1
#
# 1 <= k
# VALID
#
# res = max(4, 4)
#     = 4
#
# -----------------------------------
# r = 6
# s[r] = 'A'
#
# count['A'] = 2
#
# count = {'A': 2, 'B': 3}
#
# maxf = 3
#
# Current window:
# [B A B B A]
#
# length = 5
#
# replacements needed:
# 5 - 3 = 2
#
# 2 > k(1)
#
# INVALID.
#
# Shrink from left.
#
# Remove s[l]:
# s[2] = 'B'
#
# count['B'] = 2
#
# l = 3
#
# -----------------------------------
# Check again:
#
# Current window:
# [A B B A]
#
# length = 4
#
# 4 - 3 = 1
#
# 1 <= k
# VALID
#
# res = max(4, 4)
#     = 4
#
# -----------------------------------
# return res
#
# FINAL ANSWER = 4
#
# One valid longest substring is:
#
# "AABA"
#
# Change B -> A
#
# "AAAA"
#
# Length = 4
#
# -----------------------------------
# MAIN FORMULA TO REMEMBER:
#
# replacements needed =
#       window length - most frequent character
#
# (r - l + 1) - maxf
#
# If replacements needed <= k:
#     window is valid
#
# If replacements needed > k:
#     shrink window from left
#
# -----------------------------------
# SLIDING WINDOW MENTAL MODEL:
#
# r -> expands the window
# l -> shrinks the window
#
# count -> frequency of each character
# maxf  -> highest frequency in the window/history
#
# res -> longest valid window found
#
# -----------------------------------
# PATTERN:
#
# Expand with r
#     ↓
# Add character to count
#     ↓
# Find most frequent character
#     ↓
# Check how many replacements are needed
#     ↓
# Too many replacements?
#     ↓
# Move l until valid
#     ↓
# Update res
#
# Time: O(n)
# Space: O(1)
# (because there are only 26 uppercase English letters)