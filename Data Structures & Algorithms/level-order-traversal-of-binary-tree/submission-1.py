from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if not root:
            return res

        q = deque()
        q.append(root)
        while q:
            level = []

            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            res.append(level)

        return res
#Complexity - Time: O(n) — every node is processed once. Space: O(w) auxiliary space, where w is the maximum width of the tree; worst case O(n).