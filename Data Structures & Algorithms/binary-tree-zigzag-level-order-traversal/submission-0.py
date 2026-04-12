# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queu = deque()
        res = []
        if not root:
            return res
        queu.append(root)
        level = 0
        while queu:
            n = len(queu)
            currLevel = []
            for i in range(n):
                curr = queu.popleft()
                if not curr:
                    continue
                currLevel.append(curr.val)
                queu.append(curr.left)
                queu.append(curr.right)
            level+=1
            if level%2==0:
                currLevel = currLevel[::-1]
            if len(currLevel):

                res.append(currLevel)
        return res
                
                
        