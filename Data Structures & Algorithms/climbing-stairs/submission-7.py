class Solution:
    def climbStairs(self, n: int) -> int:
        mem={}
        def dfs(i):
            if i==n:
                return 1
            if i>n:
                return 0
            if i in mem:
                return mem[i]
            mem[i] = dfs(i+1)+dfs(i+2)
            return mem[i]
        return dfs(0)
        