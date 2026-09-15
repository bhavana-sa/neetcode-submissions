# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: #Does the root exist?, if root = None there's no tree to invert.So we return None
            return None

        queue = deque([root]) #We're creating a queue, We put the root into the queue:queue = [1]

        while queue:   #As long as there is something in the queue, keep processing
            node = queue.popleft() #popleft() removes the first item from the queue.we get:node = 1 queue = []
            node.left, node.right = node.right, node.left #actual inversion
            if node.left: #if there is a node on left
                queue.append(node.left) #Add the left child to the queue
            if node.right: #if there is a node on right
                queue.append(node.right)  #Add the right child to the queue, now queue = [3, 2]
        return root


