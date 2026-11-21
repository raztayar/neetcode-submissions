# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []

        Q = deque([(root, 0)])
        while Q:
            curr_node, l = Q.popleft()

            if len(res) - 1 < l:
                res.append([curr_node.val])
                # print("new, " , res)
            else:
                res[l].append(curr_node.val)
                # print(f"added to {l} " , res)

            if curr_node.left:
                Q.append((curr_node.left, l + 1))
            if curr_node.right:
                Q.append((curr_node.right, l + 1))
        
        return res
