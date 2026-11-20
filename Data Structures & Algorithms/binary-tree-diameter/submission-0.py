# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diam_and_height(node: Optional[TreeNode]) -> tuple[int, int]:
            if not node:
                return 0, 0
            
            d_l, h_l = diam_and_height(node.left)
            d_r, h_r = diam_and_height(node.right)

            h = 1 + max(h_l, h_r)
            d = max(d_l, d_r, h_l + h_r)

            return d, h
        
        return diam_and_height(root)[0]
