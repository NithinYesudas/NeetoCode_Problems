class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        mem={}
        n = len(nums)
        def dfs(i,flag):
            if i>=n or (flag and i == n-1):
                return 0
            if (i,flag) in mem:
                return mem[(i,flag)]
            mem[(i,flag)] = max(dfs(i+1,flag), nums[i]+dfs(i+2,flag))
            return mem[(i,flag)]
        return max(dfs(0,True),dfs(1,False))


        