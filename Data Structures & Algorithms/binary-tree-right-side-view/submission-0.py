# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        mem = {}
        def helper(node,level):
            nonlocal mem
            if not node:
                return
            level+=1
            if level not in mem:
                mem[level] = node.val
            helper(node.right,level)
            helper(node.left,level)
        helper(root,0)
        return [x for x in mem.values()]
        