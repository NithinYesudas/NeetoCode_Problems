# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        def helper(node,length):
            nonlocal depth
            if not node:
                return
            length+=1
            depth = max(depth,length)
            helper(node.left,length)
            helper(node.right,length)
        helper(root,0)
        return depth