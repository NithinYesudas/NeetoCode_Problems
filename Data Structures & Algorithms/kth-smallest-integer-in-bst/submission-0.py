# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def helper(node,count):
            nonlocal res
            if not node:
                return
            helper(node.left,count)
            res.append(node.val)
            helper(node.right,count)  
        helper(root,0)   
        return res[k-1]     
        