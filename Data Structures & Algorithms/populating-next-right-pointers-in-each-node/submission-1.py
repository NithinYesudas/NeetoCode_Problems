"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        queu = deque()
        queu.append(root)
        right = None
        while queu:
            n = len(queu)
            for i in range(n):

                curr = queu.popleft()
                curr.next = right
                if curr.right:
                    queu.append(curr.right)
                    queu.append(curr.left)
                right = curr
            right = None
        return root


        