class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        max_length = 0
        def dfs(curr,i):
            if i>=len(nums):
                return 0
            take = 0
            if curr<nums[i]:
                take = 1+dfs(nums[i],i+1)
            skip = dfs(curr,i+1)
            return max(take,skip)
        for i in range(len(nums)):
            max_length = max(max_length,dfs(nums[i],i))
        return max_length+1



        