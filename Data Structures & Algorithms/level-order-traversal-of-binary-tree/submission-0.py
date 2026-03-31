# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        mem = {}
        def helper(node,level):
            nonlocal mem
            if not node:
                return
            level+=1
            if level in mem:
                mem[level].append(node.val)
            else:
                mem[level] = [node.val]
            helper(node.left,level)
            helper(node.right,level)
        res = []
        helper(root,0)
        for item in mem.values():
            res.append(item)
        return res
        
        