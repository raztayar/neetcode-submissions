# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        Q = deque([(root, 0)])

        last_level = -1

        while Q:
            node, l = Q.popleft()
            if l > last_level:
                res.append(node.val)
                last_level += 1
                print(node.val, "is the opener for new level: ", last_level)
            
            left, right = node.left, node.right

            if right:
                Q.append((right, l + 1))
            
            if left:
                Q.append((left, l + 1))
        
        return res
        