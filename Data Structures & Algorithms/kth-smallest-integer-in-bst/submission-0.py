# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr  = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right
#What does "smallest" mean?
#Look at all the numbers in the tree: 5, 3, 7, 1, 4, 6, 8
#Put them in increasing order: 1, 3, 4, 5, 6, 7, 8
#Now we can identify their positions:
#1st → 1, 2nd → 3, 3rd → 4, 4th → 5, 5th → 6, 6th → 7, 7th → 8
        