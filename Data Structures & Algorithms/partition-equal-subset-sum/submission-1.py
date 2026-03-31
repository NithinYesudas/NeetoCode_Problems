class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2==1:
            return False
        mem = {}
        def dfs(i,target):
            if target==0:
                return True
            if i>=len(nums) or target<0:
                return False
            if (i,target) in mem:
                return mem[(i,target)]
            mem[(i,target)]= dfs(i+1,target) or dfs(i+1,target-nums[i])
            return mem[(i,target)]
        return dfs(0,sum(nums)//2)
        
        