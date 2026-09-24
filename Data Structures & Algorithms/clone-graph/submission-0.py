"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        max_to_clone = {}
        def dfs(node):
            if not node:
                return None
            if node in max_to_clone:
                return max_to_clone[node]

            clone = Node(node.val)
            max_to_clone[node] = clone

            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone
        return dfs(node)
        