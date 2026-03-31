class Solution:
    def climbStairs(self, n: int) -> int:
        mem = {}
        def dfs(i):
            if i>=n:
                return i==n
            if i in mem:
                return mem[i]
            mem[i]= dfs(i+1)+dfs(i+2)
            return mem[i]
        return dfs(0)
            
        