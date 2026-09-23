class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res += (bit << (31 - i))
        return res

        # DRY RUN
#
# Simplified 4-bit example:
#
# n = 1011
#
# We want to reverse the bits:
#
# Original:  1 0 1 1
# Position:  3 2 1 0
#
# Reversed:  1 1 0 1
# Position:  3 2 1 0
#
# Start:
# res = 0000
#
# --------------------------------------------------
# i = 0
# --------------------------------------------------
#
# We want the bit at position 0.
#
# n = 1011
#              ↑
#            bit 0
#
# bit = (n >> 0) & 1
#
# n >> 0:
#
# 1011 >> 0 = 1011
#
# Now:
#
#   1011
# & 0001
# ------
#   0001
#
# bit = 1
#
# Original position = 0
#
# Reversed position = 3 - 0 = 3
#
# Move the bit to position 3:
#
# 1 << 3 = 1000
#
# res = 0000 + 1000
#
# res = 1000
#
# --------------------------------------------------
# i = 1
# --------------------------------------------------
#
# We want the bit at position 1.
#
# n = 1011
#             ↑
#           bit 1
#
# bit = (n >> 1) & 1
#
# First shift right:
#
# 1011 >> 1 = 0101
#
# Then:
#
#   0101
# & 0001
# ------
#   0001
#
# bit = 1
#
# Original position = 1
#
# Reversed position = 3 - 1 = 2
#
# Move the bit:
#
# 1 << 2 = 0100
#
# res = 1000 + 0100
#
# res = 1100
#
# --------------------------------------------------
# i = 2
# --------------------------------------------------
#
# We want the bit at position 2.
#
# n = 1011
#           ↑
#         bit 2
#
# bit = (n >> 2) & 1
#
# Shift right:
#
# 1011 >> 2 = 0010
#
# Then:
#
#   0010
# & 0001
# ------
#   0000
#
# bit = 0
#
# Original position = 2
#
# Reversed position = 3 - 2 = 1
#
# Since bit = 0, nothing is added.
#
# res = 1100
#
# --------------------------------------------------
# i = 3
# --------------------------------------------------
#
# We want the bit at position 3.
#
# n = 1011
#           ↑
#         bit 3
#
# bit = (n >> 3) & 1
#
# Shift right:
#
# 1011 >> 3 = 0001
#
# Then:
#
#   0001
# & 0001
# ------
#   0001
#
# bit = 1
#
# Original position = 3
#
# Reversed position = 3 - 3 = 0
#
# Move the bit:
#
# 1 << 0 = 0001
#
# res = 1100 + 0001
#
# res = 1101
#
# --------------------------------------------------
# FINAL
# --------------------------------------------------
#
# Original:
# 1011
#
# Reversed:
# 1101
#
# Therefore:
#
# 1011 → 1101
        