class Solution:
    def climbStairs(self, n: int) -> int:
        mem = {}
        count =0
        def helper(curr):
            nonlocal count
            if curr == n:
                return True
            if curr>n:
                return False
            if curr in mem:
                return mem[curr]
            mem[curr] = helper(curr+1)+helper(curr+2)
            return mem[curr]
        return helper(0)
        
    
        