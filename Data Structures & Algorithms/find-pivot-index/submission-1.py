class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nums = nums.copy()
        for i in range(1,len(nums)):
            nums[i] = nums[i]+nums[i-1]
        for i in range(len(nums)):
            currDiff = nums[-1]-nums[i]
            if  currDiff== nums[i-1] or (currDiff==0 and i == 0):
                return i
        
        return -1


        