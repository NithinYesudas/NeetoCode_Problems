# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_list = []
        q_list=[]
        def helper(node, path):
            nonlocal p_list, q_list
            if not node:
                return
            path.append(node)
            if node.val == p.val :
                p_list = path.copy()
            elif q.val == node.val:
                q_list = path.copy()
            
            helper(node.left,path)
            helper(node.right,path)
            path.pop()
        helper(root,[])
        print(p_list)
        LCA=None
        for i in range(min(len(p_list),len(q_list))):
            if p_list[i]==q_list[i]:
                LCA= p_list[i]
            else: 
                break
        return LCA

        