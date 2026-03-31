# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        mem={}
        def helper(node,parentTaken):
            nonlocal mem
            if not node:
                return 0
            if (node,parentTaken) in mem:
                return mem[(node,parentTaken)]
            res = 0
            if parentTaken:
                res= helper(node.left,False)+helper(node.right,False)
            else:
                take = node.val+helper(node.left,True)+helper(node.right,True)
                skip = helper(node.left,False)+helper(node.right,False)
                res= max(take,skip)
            mem[(node,parentTaken)]=res
            return res
            

        return max(helper(root,True),helper(root,False))

        