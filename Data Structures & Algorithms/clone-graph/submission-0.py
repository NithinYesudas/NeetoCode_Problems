"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mem = {}
        def helper(node):
            if node in mem:
                return mem[node]
            copy = Node(node.val)
            mem[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(helper(n))
            return copy
        return helper(node) if node else None

        
                
            
        