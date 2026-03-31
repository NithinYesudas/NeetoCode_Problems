class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def helper(i,path):
            if len(path) == k:
                res.append(path.copy())
                return
            if i>n:
                return
            path.append(i)
            helper(i+1,path)
            path.pop()
            helper(i+1,path)
        helper(1,[])
        return res

        