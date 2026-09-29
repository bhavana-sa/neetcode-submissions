class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
# Example:
# s = "abcabcbb"
#
# Index:
#       0  1  2  3  4  5  6  7
#       a  b  c  a  b  c  b  b
#
# charSet = set()
# l = 0
# res = 0
#
# We use a SLIDING WINDOW:
#
#       l              r
#       ↓              ↓
#      [ a  b  c  ... ]
#
# The window from l to r must contain
# ONLY UNIQUE characters.
#
# -----------------------------------
# r = 0
# s[r] = 'a'
#
# Is 'a' already in charSet?
# NO
#
# Add 'a':
# charSet = {'a'}
#
# Window:
# [a]
#
# Length = r - l + 1
#        = 0 - 0 + 1
#        = 1
#
# res = max(0, 1)
#     = 1
#
# -----------------------------------
# r = 1
# s[r] = 'b'
#
# Is 'b' already in charSet?
# NO
#
# Add 'b':
# charSet = {'a', 'b'}
#
# Window:
# [a b]
#
# Length = 1 - 0 + 1
#        = 2
#
# res = max(1, 2)
#     = 2
#
# -----------------------------------
# r = 2
# s[r] = 'c'
#
# Is 'c' already in charSet?
# NO
#
# Add 'c':
# charSet = {'a', 'b', 'c'}
#
# Window:
# [a b c]
#
# Length = 2 - 0 + 1
#        = 3
#
# res = max(2, 3)
#     = 3
#
# -----------------------------------
# r = 3
# s[r] = 'a'
#
# Is 'a' already in charSet?
# YES
#
# We have a duplicate.
#
# while s[r] in charSet:
#
# Remove s[l]:
# s[l] = 'a'
#
# charSet = {'b', 'c'}
#
# Move l:
# l = 1
#
# Now:
# s[r] = 'a'
# Is 'a' in charSet?
# NO
#
# Exit while loop.
#
# Add 'a':
# charSet = {'a', 'b', 'c'}
#
# Current window:
# [b c a]
#  ↑   ↑
#  l   r
#
# Length = 3 - 1 + 1
#        = 3
#
# res = max(3, 3)
#     = 3
#
# -----------------------------------
# r = 4
# s[r] = 'b'
#
# Is 'b' already in charSet?
# YES
#
# Remove s[l]:
# s[l] = 'b'
#
# charSet = {'a', 'c'}
#
# Move l:
# l = 2
#
# Now 'b' is no longer in the set.
#
# Add 'b':
# charSet = {'a', 'b', 'c'}
#
# Window:
# [c a b]
#
# Length = 4 - 2 + 1
#        = 3
#
# res = max(3, 3)
#     = 3
#
# -----------------------------------
# r = 5
# s[r] = 'c'
#
# 'c' is already in charSet.
#
# Remove s[l]:
# s[l] = 'c'
#
# charSet = {'a', 'b'}
#
# Move l:
# l = 3
#
# Add 'c':
# charSet = {'a', 'b', 'c'}
#
# Window:
# [a b c]
#
# Length = 5 - 3 + 1
#        = 3
#
# res = max(3, 3)
#     = 3
#
# -----------------------------------
# r = 6
# s[r] = 'b'
#
# 'b' is already in charSet.
#
# Remove s[l]:
# s[l] = 'a'
#
# charSet = {'b', 'c'}
#
# Move l:
# l = 4
#
# 'b' is STILL in charSet.
#
# Remove s[l]:
# s[l] = 'b'
#
# charSet = {'c'}
#
# Move l:
# l = 5
#
# Now 'b' is NOT in charSet.
#
# Add 'b':
# charSet = {'b', 'c'}
#
# Window:
# [c b]
#
# Length = 6 - 5 + 1
#        = 2
#
# res = max(3, 2)
#     = 3
#
# -----------------------------------
# r = 7
# s[r] = 'b'
#
# 'b' is already in charSet.
#
# Remove s[l]:
# s[l] = 'c'
#
# charSet = {'b'}
#
# Move l:
# l = 6
#
# 'b' is STILL in charSet.
#
# Remove s[l]:
# s[l] = 'b'
#
# charSet = set()
#
# Move l:
# l = 7
#
# Now 'b' is NOT in charSet.
#
# Add 'b':
# charSet = {'b'}
#
# Window:
# [b]
#
# Length = 7 - 7 + 1
#        = 1
#
# res = max(3, 1)
#     = 3
#
# -----------------------------------
# return res
#
# FINAL ANSWER = 3
#
# The longest substrings without repeating
# characters include:
#
# "abc"
# "bca"
# "cab"
#
# Length = 3
#
# -----------------------------------
# IMPORTANT MENTAL MODEL:
#
# r = expands the window
# l = shrinks the window when we get a duplicate
#
# The window must ALWAYS contain unique characters.
#
# New character is unique:
#     -> add it
#
# New character is duplicate:
#     -> remove from the LEFT
#     -> keep moving l until duplicate is gone
#
# Then:
#     -> add the new character
#     -> calculate window length
#     -> update res
#
# Formula:
# window length = r - l + 1
#
# -----------------------------------
# PATTERN:
#
# "Longest/shortest substring"
# + "no repeating characters"
# -> SLIDING WINDOW
#
# Use:
# set + two pointers
#
# Time: O(n)
# Space: O(n)