class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mem = {}
        for i in range(len(nums)):
            mem[nums[i]] = i
        max_length = 0
        for num in nums:
            curr_length = 0
            while num in mem:
                curr_length+=1
                num+=1
            max_length = max(max_length,curr_length)
        return max_length
        