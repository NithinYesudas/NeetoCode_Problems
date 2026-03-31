# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        count=0
        def helper(node,maxVal):
            nonlocal count
            if not node:
                return
            if node.val>=maxVal:
                count+=1
                maxVal = node.val
            helper(node.left,maxVal)
            helper(node.right,maxVal)
        helper(root,float('-inf'))
        return count


        