# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_list = []
        q_list = []
        def dfs(node,path):
            nonlocal p_list,q_list
            if not node:
                return
            path.append(node)
            if node.val == p.val:
                p_list = path.copy()
            if node.val == q.val:
                q_list = path.copy()
            if len(p_list) and len(q_list):
                return
            dfs(node.left,path)
            dfs(node.right,path)
            path.pop()
        dfs(root,[])
        LCA = None
        for i in range(min(len(p_list),len(q_list))):

            if p_list[i].val==q_list[i].val:
                LCA=p_list[i]
            else:
                break
            
        return LCA
            

        