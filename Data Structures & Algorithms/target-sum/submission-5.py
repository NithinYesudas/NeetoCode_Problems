class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        mem = {}
        def dfs(i,currSum):
            if currSum==target and i==len(nums):
                return 1
            if i>=len(nums):
                return 0
            if (i,currSum) in mem:
                return mem[(i,currSum)]
            res = dfs(i+1, currSum+nums[i])+dfs(i+1,currSum-nums[i])
            mem[(i,currSum)] = res
            return res
        return dfs(0,0)
