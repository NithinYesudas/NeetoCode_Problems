class Solution:
    def climbStairs(self, n: int) -> int:
        mem= {}
        def helper(currSum):
            if currSum == n:
                return 1
            if currSum>n:
                return 0
            if currSum in mem:
                return mem[currSum]
            mem[currSum]= helper(currSum+1)+helper(currSum+2)
            return mem[currSum]
        return helper(0)
        