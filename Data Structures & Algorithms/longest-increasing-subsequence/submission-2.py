class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        mem = [1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[j]>nums[i]:
                    mem[i] = max(mem[i],1+mem[j])
        return max(mem)

        