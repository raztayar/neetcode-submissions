# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_level = 1
        q = deque([(root, 1)])

        while q:
            t, level = q.popleft()
            max_level = level
            l = t.left
            r = t.right

            if l:
                q.append((l, level + 1))
            if r:
                q.append((r, level + 1))
        
        return max_level


