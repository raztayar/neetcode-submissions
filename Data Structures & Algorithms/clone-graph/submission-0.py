"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}

        def dfs(v):
            if not v:
                return None
            
            copy_v = Node(v.val)
            visited[v.val] = copy_v

            for u in v.neighbors:
                if u.val not in visited:
                    copy_v.neighbors.append(dfs(u))
                else:
                    copy_v.neighbors.append(visited[u.val])
            
            return copy_v

        
        return dfs(node)
        
        
