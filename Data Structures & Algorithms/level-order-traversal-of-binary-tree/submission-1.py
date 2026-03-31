# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        mem = {}
        if not root:
            return []
        q = deque()
        q.append(root)
        res = []
        while q:
            length = len(q)
            temp = []
            for i in range(length):
                a = q.popleft()
                print(a.val)
                temp.append(a.val)
                if a.left:
                    q.append(a.left)
                if a.right:
                    q.append(a.right)
            res.append(temp)
        return res



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
        
        